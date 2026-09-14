// es-config.js — cấu hình 2 tracker đo thời lượng ước tính (PHẢI nạp TRƯỚC 2 file tracker).
// Hướng dẫn đầy đủ: ga-tracking/docs/claude_ga4_observation_setup.md
window.GA_EST_DURATION_CONFIG = {
    measurementId: 'G-RVKW6SLD1R',        // Measurement ID property QUAN SÁT (riêng, không đụng GA4 chính)
    apiSecret: 'xYKHPPlMTHqOUEd7uuW5sA',  // Measurement Protocol API secret của property quan sát
    siteId: location.hostname,            // nhãn site đi kèm mọi event
    joinMeasurementId: 'G-ELDKBDL77V',    // Measurement ID GA4 CHÍNH của 1games.io — chỉ để join ga_session_id
                                          // khi phân tích (đọc cookie _ga_ELDKBDL77V). Đổi GA4 chính thì sửa dòng này.
    debug: false                          // true khi test (log Console); production để false
};
