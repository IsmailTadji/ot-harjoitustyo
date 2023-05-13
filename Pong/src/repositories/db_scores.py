class DbScores():
    """
    Class for storing and fetching game scores

    """

    def __init__(self, connection):
        """
        Class constructor


        Args:

            connection (sqlite connection): Database connection
        """
        self.connection = connection

    def top5_scores(self):
        """
        Fetches the top5 scores from the database


        Attributes:

            leaderboard: List, contains the player names and their scores


        Returns:

            List of the player names and their scores
        """
        cursor = self.connection.cursor()

        leaderboard = cursor.execute('''SELECT name, score
                       FROM scores
                       ORDER BY score
                       DESC LIMIT 5''').fetchall()

        return [(result["name"], result["score"]) for result in leaderboard]

    def new_score(self, name, score):
        """
        Adds a new score to the database


        Args:

            name: String, name of the player
            score: Integer, score of the player
        """
        if name:
            cursor = self.connection.cursor()

            cursor.execute(''' INSERT OR IGNORE INTO scores (name,score)
                                VALUES (?,?)''', (name,score))

            self.connection.commit()
