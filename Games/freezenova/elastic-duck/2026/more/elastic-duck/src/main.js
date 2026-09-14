import * as BG from './modules/background.js';
import * as CLOTH from './modules/cloth.js';
import * as FBO from './modules/fbo.js';
import * as PRE from './modules/pre.js';
import * as LIGHTS from './modules/lights.js';
import * as MOUSE from './modules/mouse.js';
import * as FEATURES from './modules/features.js';   // DuckMath: eyes + bill
import * as GAME from './modules/game.js';            // DuckMath: clicker game layer
import * as SOUND from './modules/sound.js';          // DuckMath: quack/buy + elastic SFX
import * as BRAND from './modules/brand.js';          // DuckMath: brand-link integrity guard

let
renderer, camera, scene, lastOrientation;

function init() {

	// renderer
	renderer = new THREE.WebGLRenderer( { antialias: true } );
	renderer.setSize( window.innerWidth, window.innerHeight );

	renderer.gammaOutput = true;
	renderer.physicallyCorrectLights = true;

	renderer.shadowMap.enabled = true;
	renderer.shadowMap.type = THREE.PCFShadowMap;

	document.body.appendChild( renderer.domElement );

	window.addEventListener( 'resize', onResize );

	// scene — DuckMath navy (was near-black 0x121312)
	scene = new THREE.Scene();
	scene.background = new THREE.Color( 0x0a1626 );

	// camera
	camera = new THREE.PerspectiveCamera( 60, window.innerWidth / window.innerHeight, 0.1, 4000 );
	camera.position.set( 0, 0, - 3.2 );   // DuckMath: centred on the duck (sheen sat low)
	camera.lookAt( new THREE.Vector3() );

	// pre-calculate geometry information
	PRE.calculate();

	// initialization block;
	BG.init( scene );
	CLOTH.init( scene );

	MOUSE.init( camera, renderer.domElement );

	// DuckMath: pick feature anchors (needs PRE.vertices) and register gather ids
	FEATURES.init( scene, camera );

	FBO.init( renderer );

	// DuckMath: track pointer for pupil look
	window.addEventListener( 'mousemove', function ( e ) {
		FEATURES.setPointer(
			( e.clientX / window.innerWidth ) * 2 - 1,
			- ( ( e.clientY / window.innerHeight ) * 2 - 1 )
		);
	} );

	// dispose of calculation data
	PRE.dispose();

	// initialize light
	LIGHTS.init( scene );

	// DuckMath: clicker game (HUD + shops + save) + sound
	GAME.init();
	SOUND.init();
	BRAND.init();                    // verify/restore the brand link from char-codes
	GAME.setSound( SOUND );          // game plays buy() on purchases, syncs mute

	// DuckMath: tapping the duck bakes ducks. Record the tap point (for the
	// floating "+N") and award a click. Pointerdown covers mouse + touch.
	// NOTE: the cloth-stretch sound is NOT triggered here — it's driven by the
	// physics deformation in the render loop (see FEATURES.getActivity below), so
	// it rings through the wobble and fades as the mesh settles, like real cloth.
	renderer.domElement.addEventListener( 'pointerdown', function ( e ) {
		GAME.setTapPoint( e.clientX, e.clientY );
		GAME.tap();
		SOUND.quack();               // duck quack (same SFX as Ducky Clicker)
	} );

	// DuckMath: Space = tap a random spot on the duck (poke physics + award click).
	// Ignored while typing in an input or holding modifiers (so dev combos still work).
	window.addEventListener( 'keydown', function ( e ) {
		if ( e.code !== 'Space' && e.key !== ' ' ) return;
		const tag = ( e.target && e.target.tagName ) || '';
		if ( tag === 'INPUT' || tag === 'TEXTAREA' || e.ctrlKey || e.metaKey || e.altKey ) return;
		e.preventDefault();             // stop page scroll
		if ( e.repeat ) return;         // holding Space must NOT auto-fire — one tap per press
		MOUSE.poke();                   // squish the duck at a random point (physics → sound)
		const cx = window.innerWidth / 2 + ( Math.random() - 0.5 ) * 180;
		const cy = window.innerHeight / 2 + ( Math.random() - 0.5 ) * 180;
		GAME.setTapPoint( cx, cy );
		GAME.tap();
		SOUND.quack();
	} );

	// (physics tuning now lives inside the in-game Settings modal — see game.js)

	// start program
	animate();

}

let _loopErrLogged = false;
function animate() {

	// The whole game runs on this single rAF chain (physics, render, HUD, passive
	// income all hang off it). requestAnimationFrame is scheduled in `finally` so
	// that one thrown frame can NEVER kill the loop — otherwise a single transient
	// error would freeze the duck permanently until a reload. The first error is
	// logged once for diagnosis; repeats are swallowed to avoid console spam.
	try {

		if ( window.orientation != lastOrientation ) {

			lastOrientation = window.orientation;
			onResize();

		}

		LIGHTS.update();
		FBO.update();
		CLOTH.update( performance.now() / 1000 );   // DuckMath: animate skin shader effects
		FEATURES.update();   // DuckMath: place eyes + bill on the deformed surface
		// DuckMath: cloth-stretch sound driven by the live physics deformation —
		// loudness follows surface motion, brightness follows stretch.
		SOUND.clothFeed( FEATURES.getStretch(), FEATURES.getActivity() );
		GAME.update();       // DuckMath: passive income + HUD/shop refresh

		renderer.setRenderTarget( null );
		renderer.render( scene, camera );

	} catch ( e ) {

		if ( ! _loopErrLogged ) { _loopErrLogged = true; console.error( 'render loop frame error (loop kept alive):', e ); }

	} finally {

		requestAnimationFrame( animate );

	}

}

function onResize() {

	const w = window.innerWidth;
	const h = window.innerHeight;

	camera.aspect = w / h;
	camera.updateProjectionMatrix();

	renderer.setSize( w, h );

};

init();
