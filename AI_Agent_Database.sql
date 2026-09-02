CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE calls (
    call_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    call_start TIMESTAMP,
    call_end TIMESTAMP,
    call_status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE call_transcripts (
    transcript_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    transcript_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE ai_responses (
    response_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    response_text TEXT NOT NULL,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE call_analytics (
    analytics_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    call_duration_seconds INT,
    resolution_status VARCHAR(50),
    ai_accuracy DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE ivr_flow (
    ivr_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    menu_option VARCHAR(100),
    action_taken VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE sentiment_logs (
    sentiment_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    sentiment VARCHAR(50),
    confidence_score DECIMAL(5,2),
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE emotion_logs (
    emotion_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    emotion VARCHAR(50),
    confidence_score DECIMAL(5,2),
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE escalation_history (
    escalation_id SERIAL PRIMARY KEY,
    call_id INT REFERENCES calls(call_id),
    escalation_reason TEXT,
    escalated_to VARCHAR(100),
    escalated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE tickets (

    ticket_id VARCHAR(20) PRIMARY KEY,

    customer_issue TEXT NOT NULL,

    sentiment VARCHAR(20),

    emotion VARCHAR(20),

    status VARCHAR(20) DEFAULT 'OPEN',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


SELECT tablename
FROM pg_tables
WHERE schemaname = 'public';


SELECT * FROM calls;

SELECT * FROM users;

INSERT INTO users
(full_name, phone_number, email)
VALUES
(
'Test User',
'9999999999',
'test@test.com'
);

SELECT current_database();

SELECT user_id, full_name
FROM users;

INSERT INTO calls
(
    user_id,
    call_status
)
VALUES
(
    1,
    'ACTIVE'
);

SELECT * FROM calls ORDER BY call_id DESC;

SELECT * FROM call_transcripts ORDER BY transcript_id DESC;

SELECT * FROM calls;
SELECT * FROM call_transcripts;
SELECT * FROM sentiment_logs;
SELECT * FROM emotion_logs;
SELECT * FROM escalation_history;
SELECT * FROM ai_responses;


SELECT * FROM calls ORDER BY call_id DESC;

SELECT * FROM call_transcripts ORDER BY transcript_id DESC;

SELECT * FROM sentiment_logs ORDER BY sentiment_id DESC;

SELECT * FROM emotion_logs ORDER BY emotion_id DESC;

SELECT * FROM call_analytics ORDER BY analytics_id DESC;

SELECT * FROM ai_responses ORDER BY response_id DESC;

SELECT * FROM escalation_history ORDER BY escalation_id DESC;

SELECT * FROM tickets;

ALTER TABLE tickets
ADD COLUMN escalation_reason TEXT;
