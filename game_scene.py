# coding: utf-8


from scene import *
import ui
import time


from luck_card import LuckCard

class GameScene(Scene):
    def setup(self):
    	
        self.start_time = time.time()
        center_of_screen = self.size/2
        



        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#80acff', 
                                     parent = self, 
                                     size = self.size)
                                     

                                      
        self.school_crest = LabelNode(text = '                                !!!GLHF!!!',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.size / 4,
                                      scale = 3)
                                      
        self.start_button = SpriteNode('./assets/sprites/start_button.PNG',
                                       parent = self,
                                       position = self.size/2)
                                       
        self.school_crest = LabelNode(text = '                          Are you ready!!!',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.size / 3,
                                      scale = 3)
                                      
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.PNG',
                                       parent = self,
                                       position = back_button_position)
                                      
                                      
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(LuckCard())
            
            
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
