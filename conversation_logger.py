from postgres.dbconnection import get_connection


def save_conversation(call_id, customer, ai, sentiment, emotion):

    conn = get_connection()
    cur = conn.cursor()

    # Save Customer Message
    cur.execute(
        """
        INSERT INTO call_transcripts
        (call_id, transcript_text)
        VALUES (%s, %s)
        """,
        (
            call_id,
            f"CUSTOMER: {customer}"
        )
    )

    # Save AI Reply
    cur.execute(
        """
        INSERT INTO call_transcripts
        (call_id, transcript_text)
        VALUES (%s, %s)
        """,
        (
            call_id,
            f"AI: {ai}"
        )
    )

    conn.commit()

    cur.close()
    conn.close()