# coding: utf-8


from scene import *
import Image
import time
import ui
import console
import random

class LuckCard(Scene):
    

    def setup(self):
        self.cards_have_moved = False
        self.start_time = time.time()
        center_of_screen = self.size/2
        self.card_move_speed = 20.0
        self.c_card_move = False
        
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#80cdff', 
                                     parent = self, 
                                     size = self.size)
                                     
                                     
        self.card1_background_position = self.size/4.096
        
        self.card1_background = SpriteNode('./assets/sprites/c_card_background.PNG',
                                    parent = self,
                                    position = self.card1_background_position)
                                    
                                    


        self.card2_background = SpriteNode('./assets/sprites/c_card_background.PNG',
                                    parent = self,
                                    position = (self.size[0]/2, self.size[1]/4.096))
                                    
        
        
        
        

        self.card3_background = SpriteNode('./assets/sprites/c_card_background.PNG',
                                    parent = self,
                                    position = (self.size[0]/1.365,  self.size[1]/4.096))


                                     

        self.menu_button = SpriteNode('./assets/sprites/menu_button.PNG',
                                    parent = self,
                                    position = (self.size[0]/2, self.size[1]/1.70),
                                    alpha = 0.75)
        
                                     


        self.start_button = LabelNode(text = '                Are you ready, \n Ace is right card, King is fake card. XD',
        
     
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = (self.size[0]/2, self.size[1]/1.28),
                                      scale = 3)
        
        
        
        

        
        
    def move_card(self, random_action):
        
        if random_action == 0 :
            self.actions = [Action.sequence(Action.move_to(512.00, 187.50 , 5), Action.wait(1), Action.move_to(750.18, 187.50 , 5),Action.wait(1), Action.move_to(250, 187.50 ,5), Action.wait(0.5), Action.move_to(512.00, 187.50 , 5), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(512.00, 187.50 , 5), Action.wait(0.5), Action.move_to(250, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,2)), Action.sequence(Action.wait(7), Action.move_to(750, 187.5 , 5), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(512, 187.50 ,2), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,2), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2)), Action.sequence(Action.move_to(512.00, 187.50 , 5), Action.wait(1), Action.move_to(250, 187.50 , 5), Action.wait(1), Action.move_to(512, 187.50 ,5), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.50 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.move_to(500, 187.5 ,2))]
        
            self.card1_background.run_action(self.actions[0])
            self.card2_background.run_action(self.actions[1])
            self.card3_background.run_action(self.actions[2])
        
        if random_action == 1:
            self.actions = [Action.sequence(Action.move_to(512.00, 187.50 , 5), Action.wait(1), Action.move_to(750.18, 187.50 , 5),Action.wait(1), Action.move_to(250, 187.50 ,5), Action.wait(0.5), Action.move_to(512.00, 187.50 , 5), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(750, 187.50 , 5), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.move_to(750, 187.5 ,3)), Action.sequence(Action.wait(7), Action.move_to(500, 187.5 , 5), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(512, 187.50 ,2), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.move_to(500, 187.5 ,3)), Action.sequence(Action.move_to(512.00, 187.50 , 5), Action.wait(1), Action.move_to(250, 187.50 , 5), Action.wait(1), Action.move_to(512, 187.50 ,5), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.50 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,2), Action.wait(0.5), Action.move_to(251, 187.5 ,3))]
        
            self.card1_background.run_action(self.actions[0])
            self.card2_background.run_action(self.actions[1])
            self.card3_background.run_action(self.actions[2])
        if random_action == 2:
            self.actions = [Action.sequence(Action.move_to(512.00, 187.50 , 5), Action.wait(1), Action.move_to(750.18, 187.50 , 5),Action.wait(1), Action.move_to(250, 187.50 ,5), Action.wait(0.5), Action.move_to(512.00, 187.50 , 5), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(750, 187.50 , 5), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,2), Action.move_to(500, 187.5, 2)), Action.sequence(Action.wait(7), Action.move_to(500, 187.5 , 5), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(512, 187.50 ,2), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.move_to(500, 187.5 ,3), Action.move_to(250, 187.5, 2)), Action.sequence(Action.move_to(512.00, 187.50 , 5), Action.wait(1), Action.move_to(250, 187.50 , 5), Action.wait(1), Action.move_to(512, 187.50 ,5), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.50 ,3), Action.wait(0.5), Action.move_to(750, 187.5 ,3), Action.wait(0.5), Action.move_to(250, 187.5 ,3), Action.wait(0.5), Action.move_to(500, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2), Action.wait(0.5), Action.move_to(250, 187.5 ,2), Action.wait(0.5), Action.move_to(750, 187.5 ,2))]
        
            self.card1_background.run_action(self.actions[0])
            self.card2_background.run_action(self.actions[1])
            self.card3_background.run_action(self.actions[2])



    

        
        

    
    def update(self):
    
    
        
        if time.time() - self.start_time > 2 and time.time() - self.start_time < 4:
            self.card1_background.texture = Texture('./assets/sprites/fake_card.PNG')
            self.card2_background.texture = Texture('./assets/sprites/right_card.PNG')
            self.card3_background.texture = Texture('./assets/sprites/fake_card.PNG')
        if time.time() - self.start_time > 4 and time.time() - self.start_time < 4.1:
            self.card1_background.texture = Texture('./assets/sprites/c_card_background.PNG')
            self.card2_background.texture = Texture('./assets/sprites/c_card_background.PNG')
            self.card3_background.texture = Texture('./assets/sprites/c_card_background.PNG')
        
        if time.time() - self.start_time <6 and time.time() - self.start_time > 4:
            if self.cards_have_moved == False:
                self.move_card(random.randint(0,3))
                self.cards_have_moved = True
            
        
        
        

        
            
            
            
            
            

            

        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        
        if time.time() - self.start_time > 10:
            if self.c_card_move == False:
                if self.card1_background.frame.contains_point(touch.location):
                    self.card1_background.texture = Texture('./assets/sprites/fake_card.PNG')
                    self.card2_background.texture = Texture('./assets/sprites/right_card.PNG')
                    self.card3_background.texture = Texture('./assets/sprites/fake_card.PNG')
                
                    self.c_card_move = True
                    console.alert('You lose', '','Ok',hide_cancel_button = True)
            if self.c_card_move == False:
                if self.card2_background.frame.contains_point(touch.location):
                    self.card1_background.texture = Texture('./assets/sprites/fake_card.PNG')
                    self.card2_background.texture = Texture('./assets/sprites/right_card.PNG')
                    self.card3_background.texture = Texture('./assets/sprites/fake_card.PNG')
                
                    self.c_card_move = True
                    console.alert('You win', '','Ok',hide_cancel_button = True)
            
        
            if self.c_card_move == False:
                if self.card3_background.frame.contains_point(touch.location):
                    self.card1_background.texture = Texture('./assets/sprites/fake_card.PNG')
                    self.card2_background.texture = Texture('./assets/sprites/right_card.PNG')
                    self.card3_background.texture = Texture('./assets/sprites/fake_card.PNG')
                
                    self.c_card_move = True
                    console.alert('you lose', '','Ok',hide_cancel_button = True)
                    
        else:
            pass
            


        
        if self.menu_button.frame.contains_point(touch.location):
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





