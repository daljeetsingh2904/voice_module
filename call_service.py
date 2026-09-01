from postgres.dbconnection import get_connection


def create_call():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO calls
        (user_id, call_status)
        VALUES (%s, %s)
        RETURNING call_id;
        """,
        (
            1,
            "ACTIVE"
        )
    )

    call_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return call_id


def end_call(call_id, status="COMPLETED"):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE calls
        SET
            call_end = CURRENT_TIMESTAMP,
            call_status = %s
        WHERE call_id = %s
        """,
        (
            status,
            call_id
        )
    )

    conn.commit()

    cur.close()
    conn.close()