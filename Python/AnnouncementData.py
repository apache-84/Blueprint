from Announcement import Announcement

def postAnnouncement(ann: Announcement):
    """
    Get Announcement object and write to database.
    """
    pass


def getAnnouncement(annID: int) -> Announcement:
    """
    Query the Announcements table and construct an Announcement object.
    """
    pass 

def getReactions(annID: int) -> int:
    """
    Query the announcementReactions table and get reactions as an int.
    Should be called when an announcement is already being displayed and someone has reacted to it since it was constructed.
    """
    pass

def updateReactions(stuID: int, annID: int):
    """
    Should allow a student to react to an announcement. Update announcementReactions table.
    """