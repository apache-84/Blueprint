from Announcement import Announcement
from db_queries import *

def postAnnouncement(ann: Announcement, facID: int):
    """
    Given an Announcement object and a faculty ID, adds the announcement to the database.

    :param ann: The Announcement object to write to the database.
    :param facID: The faculty ID of the faculty member who made the announcement.
    """
    aid = ann.getAnnID()
    text = ann.getAnnText()
    date = ann.getAnnDate()
    cid = ann.getCourse()
    
    sql = "insert into Announcements values (?, ?, ?, ?, ?)"
    fetch_query(sql, aid, text, date, cid, facID)
    print("Announcement for ", cid, " posted to database!")


def getAnnouncement(annID: int) -> Announcement:
    """
    Gets all data for the course given a announcement ID, retrieves it from the database, and constructs an Announcement object.

    :param annID: The announcement ID of the announcement to construct.
    :return: The constructed Announcement class object.
    """
    sql = "select * from Announcements where AnnouncementID = ?"
    res = fetch_query(sql, annID)
    if len(res == 0):
        print("Announcement with ID ", annID, " doesn't exist")
        return

    res = res[0]
    reactions = getReactions(annID)
    
    a = Announcement(res[0], res[1], res[2], res[3], reactions)
    return a
     

def getReactions(annID: int) -> int:
    """
    Gets the reaction state of an announcement as an int.

    Positive if there are more upvotes than downvotes, negative if vice versa.
    Gets all data from querying AnnouncementReactions table.
    Should be called when an announcement is being retried, or when someone has reacted to it since it was constructed.
    :return: The reaction state of the announcement (total upvotes - total downvotes).
    """
    sql = """select reaction, count(*) 
          from AnnouncementReactions 
          where AnnouncementID = ? 
          group by reaction 
          order by reaction desc"""
    
    res = fetch_query(sql, annID)
    upvotes = res[0][1]
    downvotes = res[1][1]
    
    reactions = upvotes - downvotes
    
    return reactions

def getNextID() -> int:
    """
    Finds the next announcementID to use in the database.

    The next announcementID will be 1 greater than the maximum ID value already existing within 
    the Announcements table in the database.
    :return: The announcementID to be used for the next announcement.
    """
    sql = "select max(announcementID) from Announcements"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id