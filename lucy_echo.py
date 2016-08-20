"""
Copyright (c) 2015. Docentron PTY LTD. All rights reserved.
This material may not be reproduced, displayed, modified or distributed without
the express prior written permission of the copyright holder.

Lucy Echo Bot
Echo back messages received to senders for a chapter chat channel.

This sample illustrates how to use the API to get messages received and send a reply to the sender for a chapter you created.

First thing to do:
    You need to first create an account at https:/www.a.kopo.com/wp/mes
    Next, create a journey using the designer. Click designer after login and add a journey.
    Next, create a chapter for the journey. In the chapter list, click the option icon (top-left in the table) and tick the id.
        Get the id of the chapter. This is the chapter_id you need.

How to use this code:
    Option 1 using Pycharm:
        Just copy this file to your Pycharm project folder and you willl see lucybot.py file under your project.
        Change username, passwd, and chapter_id below.
        Shift-Ctr-F10 to start to process your chapter messages.
        To stop your script on Pycharm, click on the stop button on the right of the Run console.
        Monitor any errors
        Modify the code to make it more interesting

    Option 2 using any text editor:
        Change username, passwd, and chapter_id below.
        Suppose you have install Pyhton 2.7 in C:/python27
        You can run this code directly using command line:
            C:\python27\python lucybot.py
        To stop your script, press Ctrl-C

"""
#================================================
# Global variables that you need to change
username = "shadows22"  # change this to your username
passwd = "Shadows22"    # change this to your passwd
chapter_id = 301          # change this to your chapter ID. It is INT type.
pathToDataFolder = "c:/dataFolder"  # change this to the folder where you want to place downloaded files for processing

#================================================
# import libraries
__author__ = 'Docentron PTY LTD'
import time
from lucy.message import Message

#================================================
# function definitions
def makeReply(msg, fdata=None):
    """
    Compose a reply of the message.
    Use all information we have to provide the best reply for the msg that can help the student

    :param msg: the message for which we need to reply
    :param fdata: file data attached to the message if any
    :param classifier: classifier if any
    :param vocab: vocabulary if any
    :param vocabibf: idf of each terms in the vocab if any
    :return: the message content for the receiver.
    """
    # do something amazing to generate the content for msg

    content = msg['content']  # need to do more than this...
    return content

def buildDatabase(messages):
    # this is called when retrieved messages from the server
    # we can save the messages to a local database and analyse patterns of users
    # use the database in makeReply function to serve the users better
    pass

#================================================
# this is where the program starts
if __name__ == '__main__':
    # create LUCY API object with your username and password for a chapter (lesson) of a journey
    # You will need to create a journey and add a chapter to the journey at KOPO MES. Get the chapter ID as the lesson_id
    # The chapter should NOT contain any questions.
    lucy = Message(username = username, passwd = passwd, lesson_id = chapter_id, pathToDataFolder = pathToDataFolder)
    lucy.processMessages(makeReply, buildDatabase)

    # what other things you can do?
    # Save retrieved messages
    #   build database of messages for each user
    #   learn behavior, preference, patterns of the users
    #   use the database to compose reply messages to help guide the students
    # Perform actions requested by users. E.g., searching google for answers
