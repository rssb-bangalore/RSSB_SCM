# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:48:52 2019

@author: Rana Rajput
"""
import logging

class Log: 
  
    __instance = None
    
    @staticmethod 
    def logger():
        """ Static access method. """
        if Log.__instance == None:
            Log()
        return Log.__instance
    
    def __init__(self):
        """ Virtually private constructor. """
        if Log.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            #Create and configure logger 
            #Setting the threshold of logger to INFO 
            logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s \n\r',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='/opt/logs/automation.log',
                    filemode='a')

            #Creating an object 
            Log.__instance = logging.getLogger() 
    
    @staticmethod 
    def info(msg):
        #print (msg)
        Log.logger().info(msg)

    @staticmethod 
    def error(msg):
        Log.logger().error(msg)
        
    @staticmethod 
    def debug(msg):
        Log.logger().debug(msg)