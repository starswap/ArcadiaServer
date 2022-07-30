from db import get_db

def check_and_assign_badge(user_name, arcade_id, score):
    db, cur = get_db()
    #if users score is highest in arcade give them a badge
    # user cant get badge if they already have it
    # user can only get badge if they are the highest scorer
    cur.execute('SELECT UserID FROM "Users" WHERE UserName=%s;', (user_name,))
    user_id = cur.fetchone()
    cur.execute('SELECT UserID, Score FROM "Scores" WHERE ArcadeId =%s ORDER BY Score;', (arcade_id,))   
    high_scorer, saved_score = cur.fetchone()
    cur.execute('SELECT BadgeID FROM "Badges" WHERE BadgeName=%s;', ("High Scorer",))
    badge_id = cur.fetchone()
    if high_scorer != user_id and saved_score < score:
        cur.execute(('INSERT INTO "UserBadges" (UserID, BadgeID) VALUES (%s, %s);'),(user_id, badge_id))
        response = "You have earned a badge!"
        return response
    else:
        response = "You did not earn a badge!"
        return response