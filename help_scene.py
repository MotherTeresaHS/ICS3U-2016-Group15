# Created by: steven
# Created on: Nov 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui




class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#80acff', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.start_button = LabelNode(text = '                                  Design by: Steven',
        
     
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.size / 3.5,
                                      scale = 3)
                                      
        self.start_button = LabelNode(text = '                                        Art work from: http://opengameart.org \n                                                 especially thank for Byron Knoll',
        
     
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.size / 6,
                                      scale = 3)
                                      
        self.school_crest = LabelNode(text = 'Computer will give you 2 same card, \n    but card total is 3  and then \n     use you eyes try to find \nthe specially card (only have one)',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = self.size / 1.8,
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
    
