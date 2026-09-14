function GameManager(size, InputManager, Actuator, StorageManager) {
  this.size = size; // Size of the grid
  this.inputManager = new InputManager;
  this.storageManager = new StorageManager;
  this.actuator = new Actuator;
  this.startTiles = 2;
  this.inputManager.on("move", this.move.bind(this));
  this.inputManager.on("restart", this.restart.bind(this));
  this.inputManager.on("keepPlaying", this.keepPlaying.bind(this));
  this.setup();
  this.audioList = {
    2: "./25051605/sound/2.mp3",
    4: "./25051605/sound/4.mp3",
    8: "./25051605/sound/8.mp3",
    16: "./25051605/sound/16.mp3",
    32: "./25051605/sound/32.mp3",
    64: "./25051605/sound/64.mp3",
    128: "./25051605/sound/128.mp3",
    256: "./25051605/sound/256.mp3",
    512: "./25051605/sound/512.mp3",
    1024: "./25051605/sound/1024.mp3",
    2048: "./25051605/sound/2048.mp3",
    4096: "./25051605/sound/4096.mp3",
    8192: "./25051605/sound/8192.mp3",
  };
  this.audio = null;
  this.audioBgStatus = true;
}

// Restart the game
GameManager.prototype.restart = function () {
  this.storageManager.clearGameState();
  this.actuator.continueGame(); // Clear the game won/lost message
  this.setup();
};

// Keep playing after winning (allows going over 2048)
GameManager.prototype.keepPlaying = function () {
  this.keepPlaying = true;
  this.actuator.continueGame(); // Clear the game won/lost message
};

// Return true if the game is lost, or has won and the user hasn't kept playing
GameManager.prototype.isGameTerminated = function () {
  return this.over || (this.won && !this.keepPlaying);
};

// Set up the game
GameManager.prototype.setup = function () {
  var previousState = this.storageManager.getGameState();

  // Reload the game from a previous game if present
  if (previousState) {
    this.grid = new Grid(previousState.grid.size,
      previousState.grid.cells); // Reload grid
    this.score = previousState.score;
    this.over = previousState.over;
    this.won = previousState.won;
    this.keepPlaying = previousState.keepPlaying;
    this.valueAudio = previousState.valueAudio;
  } else {
    this.grid = new Grid(this.size);
    this.score = 0;
    this.over = false;
    this.won = false;
    this.keepPlaying = false;
    this.valueAudio = 2;
    // Add the initial tiles
    this.addStartTiles();
  }

  // Update the actuator
  this.actuate();
};

// Set up the initial tiles to start the game with
GameManager.prototype.addStartTiles = function () {
  for (var i = 0; i < this.startTiles; i++) {
    this.addRandomTile();
  }
};

// Adds a tile in a random position
GameManager.prototype.addRandomTile = function () {
  if (this.grid.cellsAvailable()) {
    var value = Math.random() < 0.9 ? 2 : 4;
    var tile = new Tile(this.grid.randomAvailableCell(), value);

    this.grid.insertTile(tile);
  }
};

// Sends the updated grid to the actuator
GameManager.prototype.actuate = function () {
  if (this.storageManager.getBestScore() < this.score) {
    this.storageManager.setBestScore(this.score);
  }

  // Clear the state when the game is over (game over only, not win)
  if (this.over) {
    this.storageManager.clearGameState();
  } else {
    this.storageManager.setGameState(this.serialize());
  }

  this.actuator.actuate(this.grid, {
    score: this.score,
    over: this.over,
    won: this.won,
    valueAudio: this.valueAudio,
    bestScore: this.storageManager.getBestScore(),
    terminated: this.isGameTerminated()
  });

};

// Represent the current game as an object
GameManager.prototype.serialize = function () {
  return {
    grid: this.grid.serialize(),
    score: this.score,
    over: this.over,
    won: this.won,
    valueAudio: this.valueAudio,
    keepPlaying: this.keepPlaying
  };
};

// Save all tile positions and remove merger info
GameManager.prototype.prepareTiles = function () {
  this.grid.eachCell(function (x, y, tile) {
    if (tile) {
      tile.mergedFrom = null;
      tile.savePosition();
    }
  });
};

// Move a tile and its representation
GameManager.prototype.moveTile = function (tile, cell) {
  this.grid.cells[tile.x][tile.y] = null;
  this.grid.cells[cell.x][cell.y] = tile;
  tile.updatePosition(cell);
};
//ktmanh edit
//Enable audio

GameManager.prototype.playBgAudio = function () {
  let audioLink = "./25051605/sound/bg.mp3";
  if (this.gameAudio) {
    return this.gameAudio.play();
  }
  this.gameAudio = new Audio(audioLink);
  this.gameAudio.volume = 0.5;
  this.gameAudio.addEventListener('loadeddata', () => {
    this.gameAudio.play();
  });
  this.gameAudio.addEventListener('ended', (e) => {
    this.gameAudio.play();
  });
  this.gameAudio.addEventListener('error', (e) => {
    console.error("Can't playing audio:", e);
  });
}

GameManager.prototype.stopBgAudio = function () {
  if (this.gameAudio) {
    this.gameAudio.pause();
  }
}

GameManager.prototype.playAudio = function (value, isOverwrite) {
  if (!audioStatus) return;
  //Nếu có cái merge mới >= 64 thì auto chạy cái mới
  if (this.audio && isOverwrite) {
    this.audio.pause();
    this.audio.currentTime = 0;
    this.audio = null;
    // console.log("Stop current song and play new song")
  }
  //nếu không có cái mới và < 64 thì chạy hết cái cũ đã
  if (this.audio && !this.audio.paused) {
    return
  };
  let audioLink = this.audioList[value]
  this.audio = new Audio(audioLink);
  this.audio.volume = 0.75;
  this.audio.addEventListener('loadeddata', () => {
    // Audio is loaded and ready to play
    this.audio.play();
  });
  this.audio.addEventListener('error', (e) => {
    console.error("Can't playing audio:", e);
  });
}

GameManager.prototype.stopAudio = function () {
  if (this.audio) {
    this.audio.pause();
  }
}

///
// Move tiles on the grid in the specified direction
GameManager.prototype.move = function (direction) {
  // 0: up, 1: right, 2: down, 3: left
  var self = this;

  if (this.isGameTerminated()) return; // Don't do anything if the game's over
  if (this.audioBgStatus && audioStatus) {
    this.playBgAudio();
    this.audioBgStatus = false;
  }

  var cell, tile;

  var vector = this.getVector(direction);
  var traversals = this.buildTraversals(vector);
  var moved = false;
  var mergeMove = [];
  var isNew = false;
  let me = this;
  // Save the current tile positions and remove merger information
  this.prepareTiles();

  // Traverse the grid in the right direction and move tiles
  traversals.x.forEach(function (x) {
    traversals.y.forEach(function (y) {
      cell = { x: x, y: y };
      tile = self.grid.cellContent(cell);

      if (tile) {
        var positions = self.findFarthestPosition(cell, vector);
        var next = self.grid.cellContent(positions.next);

        // Only one merger per row traversal?
        if (next && next.value === tile.value && !next.mergedFrom) {
          var merged = new Tile(positions.next, tile.value * 2);
          merged.mergedFrom = [tile, next];
          mergeMove.push(merged.value);
          //When has new
          if (merged.value > me.valueAudio && merged.value >= 64) {
            isNew = true;
            me.valueAudio = merged.value;
          }

          self.grid.insertTile(merged);
          self.grid.removeTile(tile);

          // Converge the two tiles' positions
          tile.updatePosition(positions.next);

          // Update the score
          self.score += merged.value;

          // The mighty 2048 tile
          if (merged.value === 2048) self.won = true;
        } else {
          self.moveTile(tile, positions.farthest);
        }

        if (!self.positionsEqual(cell, tile)) {
          moved = true; // The tile moved from its original cell!
        }
      }
    });
  });
  let maxMergeMove = mergeMove.max();
  me.playAudio(maxMergeMove, isNew)
  //
  if (moved) {
    this.addRandomTile();

    if (!this.movesAvailable()) {
      this.over = true; // Game over!
    }
    this.actuate();
  }
};
Array.prototype.max = function () {
  if (!this.length) return null;
  return Math.max.apply(null, this);
};

Array.prototype.min = function () {
  return Math.min.apply(null, this);
};
// Get the vector representing the chosen direction
GameManager.prototype.getVector = function (direction) {
  // Vectors representing tile movement
  var map = {
    0: { x: 0, y: -1 }, // Up
    1: { x: 1, y: 0 },  // Right
    2: { x: 0, y: 1 },  // Down
    3: { x: -1, y: 0 }   // Left
  };

  return map[direction];
};

// Build a list of positions to traverse in the right order
GameManager.prototype.buildTraversals = function (vector) {
  var traversals = { x: [], y: [] };

  for (var pos = 0; pos < this.size; pos++) {
    traversals.x.push(pos);
    traversals.y.push(pos);
  }

  // Always traverse from the farthest cell in the chosen direction
  if (vector.x === 1) traversals.x = traversals.x.reverse();
  if (vector.y === 1) traversals.y = traversals.y.reverse();

  return traversals;
};

GameManager.prototype.findFarthestPosition = function (cell, vector) {
  var previous;

  // Progress towards the vector direction until an obstacle is found
  do {
    previous = cell;
    cell = { x: previous.x + vector.x, y: previous.y + vector.y };
  } while (this.grid.withinBounds(cell) &&
    this.grid.cellAvailable(cell));

  return {
    farthest: previous,
    next: cell // Used to check if a merge is required
  };
};

GameManager.prototype.movesAvailable = function () {
  return this.grid.cellsAvailable() || this.tileMatchesAvailable();
};

// Check for available matches between tiles (more expensive check)
GameManager.prototype.tileMatchesAvailable = function () {
  var self = this;

  var tile;

  for (var x = 0; x < this.size; x++) {
    for (var y = 0; y < this.size; y++) {
      tile = this.grid.cellContent({ x: x, y: y });

      if (tile) {
        for (var direction = 0; direction < 4; direction++) {
          var vector = self.getVector(direction);
          var cell = { x: x + vector.x, y: y + vector.y };

          var other = self.grid.cellContent(cell);

          if (other && other.value === tile.value) {
            return true; // These two tiles can be merged
          }
        }
      }
    }
  }

  return false;
};

GameManager.prototype.positionsEqual = function (first, second) {
  return first.x === second.x && first.y === second.y;
};
