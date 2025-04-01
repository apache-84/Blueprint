from Announcement import Announcement
from db_queries import *

def postAnnouncement(ann: Announcement, facID: int):
    """
    Get Announcement object and write to database.
    """
    aid = ann.getAnnID()
    text = ann.getAnnText()
    date = ann.getAnnDate()
    cid = ann.getCourse()
    
    sql = "insert into Announcements values (?, ?, ?, ?, ?)"
    fetch_query(sql, aid, text, date, cid, facID)
    pass


def getAnnouncement(annID: int) -> Announcement:
    """
    Query the Announcements table and construct an Announcement object.
    """
    sql = "select * from Announcements where AnnouncementID = ?"
    res = fetch_query(sql, annID)[0]
    reactions = getReactions(annID)
    
    a = Announcement(res[0], res[1], res[2], res[3], reactions)
    return a
     

def getReactions(annID: int) -> int:
    """
    Query the announcementReactions table and get reactions as an int.
    Should be called when an announcement is already being displayed and someone has reacted to it since it was constructed.
    """
    sql = """select reaction, count(*) 
          from AnnouncementReactions 
          where AnnouncementID = ? 
          group by reaction 
          order by reaction desc"""
    
    # 1 then 0
    res = fetch_query(sql, annID)
    upvotes = res[0][1]
    downvotes = res[1][1]
    
    reactions = upvotes - downvotes
    
    pass

def updateReactions(stuID: int, annID: int):
    """
    Should allow a student to react to an announcement. Update announcementReactions table.
    """