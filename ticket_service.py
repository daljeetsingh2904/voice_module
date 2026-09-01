from postgres.dbconnection import get_connection


def generate_ticket_id():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) 
        FROM tickets;
        """
    )

    count = cursor.fetchone()[0]

    ticket_number = count + 1

    ticket_id = f"TKT{ticket_number:06d}"

    cursor.close()
    conn.close()

    return ticket_id



def create_ticket(
        customer_issue,
        sentiment,
        emotion,
         escalation_reason
):

    ticket_id = generate_ticket_id()

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO tickets
        (
            ticket_id,
            customer_issue,
            sentiment,
            emotion,
            status,
            escalation_reason
        )

        VALUES
        (%s,%s,%s,%s,%s,%s)

        """,
        (
            ticket_id,
            customer_issue,
            sentiment,
            emotion,
            "OPEN",
            escalation_reason
        )
    )


    conn.commit()

    cursor.close()
    conn.close()


    return ticket_id