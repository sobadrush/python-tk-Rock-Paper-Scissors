from tkinter import *
import random

class GAMING_INTERFACE:
    
    def __init__(self):

        self.GAME_WIDTH, self.GAME_HEIGHT = 1440, 720
        self.PAPER_IMG_PATH = './img/paper.png'
        self.SCISSORS_IMG_PATH = './img/scissors.png'
        self.STONE_IMG_PATH = './img/stone.png'
        self.USER_IMG_PATH = './img/user.png'
        self.ROBOT_IMG_PATH = './img/robot.png'
        self.TILTE_FRAME_BACKGROUND = 'white'
        self.USER_FRAME_BACKGROUNG = 'white'
        self.ROBOT_FRAME_BACKGROUNG = 'white'
        self.RESULT_FRAME_BACKGROUNG = 'black'
        self.USER_BUTTON_LIGHT_COLOR = '#FFCBB3'
        self.USER_BUTTON_DARK_COLOR = '#D94600'
        self.ROBOT_BUTTON_COLOR = '#FFCBB3'
        self.RESET_BUTTON_DARK_COLOR = '#D94600'
        self.RESET_BUTTON_LIGHT_COLOR = '#FFCBB3'
        self.user_points = 0 # 玩家分數
        self.robot_points = 0 # 電腦分數

    def run(self):
        
        root = Tk()
        
        ####### GUI settings #######
        root.configure( bg='grey' )# 背景顏色
        root.geometry(f'{self.GAME_WIDTH}x{self.GAME_HEIGHT}')# 視窗大小
        root.title('剪刀石頭布')# 視窗標題
        root.resizable(False,False)# 固定視窗大小
        ####### END #######
        
        ####### IMAGE settings #######
        self.__load_img()# 載入圖片
        ####### END #######
        
        ####### title_frame #######
        self.title_frame = self.__set_title_frame(root) # 設定標題
        self.title_frame.place( x=0 ,y=0 )# 放置標題
        ####### END #######
        
        ####### user_frame #######
        self.user_frame, self.user_scissors_btn, self.user_stone_btn, self.user_paper_btn, self.user_points_var = self.__set_user_frame(root)# 設定玩家的畫面
        # 放置玩家的畫面
 
        self.__changeOnHover(self.user_scissors_btn, self.USER_BUTTON_LIGHT_COLOR,  self.USER_BUTTON_DARK_COLOR)
        self.__changeOnHover(self.user_stone_btn, self.USER_BUTTON_LIGHT_COLOR,  self.USER_BUTTON_DARK_COLOR)
        self.__changeOnHover(self.user_paper_btn,  self.USER_BUTTON_LIGHT_COLOR,  self.USER_BUTTON_DARK_COLOR)
        ####### END #######
        '''
        ####### robot_frame #######
        self.robot_frame, self.robot_scissors_label, self.robot_stone_label, self.robot_paper_label, self.robot_points_var = # 設定電腦的畫面
        # 放置電腦的畫面
        ####### END #######

        ####### result_frame #######
        self.result_frame,self.result = # 設定結果的畫面
        ####### END #######
        '''
        root.mainloop()
    
    def __load_img(self): # 載入圖片
        
        self.user_img = PhotoImage( file=self.USER_IMG_PATH ).zoom(18).subsample(30)
        
        self.robot_img = PhotoImage(file=self.ROBOT_IMG_PATH).zoom(13).subsample(30)
        
        self.scissors_img = PhotoImage(file=self.SCISSORS_IMG_PATH).zoom(10).subsample(30)#載入剪刀圖片
        self.stone_img = PhotoImage(file=self.STONE_IMG_PATH).zoom(10).subsample(30)#載入石頭圖片
        self.paper_img = PhotoImage(file=self.PAPER_IMG_PATH).zoom(10).subsample(30)#載入布圖片
        
    
    def __set_title_frame(self, root): # 設定標題
        
        title_frame = Frame( root, bg=self.TILTE_FRAME_BACKGROUND, width=self.GAME_WIDTH, height=self.GAME_HEIGHT*0.2, highlightthickness='5' ) # 設定標題的框架
        
        title_label = Label( title_frame, bg='white', width=45, height=2, font=('Arial',40), fg='black', text='Paper Scissors Stone',highlightbackground='blue' ) # 設定標題的標籤
        title_label.place( x=15, y=4 ) # 放置標題的標籤
        
        return title_frame
    
    def __set_user_frame(self,root):
        
        user_frame = Frame( root, bg=self.USER_FRAME_BACKGROUNG, width=self.GAME_WIDTH*0.5, height=self.GAME_HEIGHT*0.8, highlightthickness='3' ) # 設定玩家的框架

        user_img_label = Label( user_frame, bg=self.USER_FRAME_BACKGROUNG, width=300, height=200, image=self.user_img, text='user image' ) # 設定玩家的圖片
        user_img_label.place( x=self.GAME_WIDTH*0.25, y=30, anchor='n' ) # 放置玩家的圖片

        user_scissors_btn = Button( user_frame, image=self.scissors_img, text= 'scissors', state=NORMAL, command=self.__click_scissors, relief='groove', background=self.USER_BUTTON_DARK_COLOR, activebackground=self.USER_BUTTON_LIGHT_COLOR, fg=self.USER_BUTTON_LIGHT_COLOR, activeforeground=self.USER_BUTTON_DARK_COLOR ) # 設定剪刀按鈕
        user_scissors_btn.place( x=140, y=400 ,anchor='center') # 放置剪刀按鈕

        user_stone_btn = Button( user_frame, image=self.stone_img, text='stone', state=NORMAL, command=self.__click_stone, relief='groove', background=self.USER_BUTTON_DARK_COLOR, activebackground=self.USER_BUTTON_LIGHT_COLOR, fg=self.USER_BUTTON_LIGHT_COLOR, activeforeground=self.USER_BUTTON_DARK_COLOR )# 設定石頭按鈕
        user_stone_btn.place( x=360, y=400 ,anchor='center')# 放置石頭按鈕

        user_paper_btn = Button( user_frame, image=self.paper_img, text='paper', state=NORMAL, command=self.__click_paper, relief='groove', background=self.USER_BUTTON_DARK_COLOR, activebackground=self.USER_BUTTON_LIGHT_COLOR, fg=self.USER_BUTTON_LIGHT_COLOR, activeforeground=self.USER_BUTTON_DARK_COLOR )# 設定布按鈕
        user_paper_btn.place( x=580, y=400 ,anchor='center')# 放置布按鈕

        user_points_var = StringVar() # 設定玩家的分數
        user_points_var.set('') # 設定玩家的分數
        user_points_label = Label( user_frame, bg=self.USER_FRAME_BACKGROUNG, textvariable=user_points_var,font=('Arial',30), fg='black' ) # 設定玩家的分數
        user_points_label.place( x=self.GAME_WIDTH*0.25, y=250, anchor='n' ) # 放置玩家的分數

        return user_frame, user_scissors_btn, user_stone_btn, user_paper_btn, user_points_var
    '''
    def __set_robot_frame(self,root):
        
        robot_frame = Frame( root, bg=self.ROBOT_FRAME_BACKGROUNG, width=self.GAME_WIDTH*0.5, height=self.GAME_HEIGHT*0.8, highlightthickness='3' ) # 設定電腦的框架
        
        robot_img_label = Label( robot_frame, bg=self.ROBOT_FRAME_BACKGROUNG, image=self.robot_img, text='robot_img', width=300, height=200 ) # 設定電腦的圖片
        robot_img_label.place( x=self.GAME_WIDTH*0.25, y=30, anchor='n' ) # 放置電腦的圖片
        
        robot_scissors_label = Label( robot_frame, image=self.scissors_img, text='scissors', background=self.ROBOT_BUTTON_COLOR ) # 設定電腦的剪刀
        robot_scissors_label.place( x=140, y=400, anchor='center' ) # 放置電腦的剪刀
        
        robot_stone_label = # 設定電腦的石頭
        # 放置電腦的石頭
        
        robot_paper_label = # 設定電腦的布
        # 放置電腦的布

        robot_points_var = StringVar() # 設定電腦的分數
        robot_points_var.set('') # 設定電腦的分數
        robot_points_label =  # 設定電腦的分數
        # 放置電腦的分數

        return robot_frame, robot_scissors_label, robot_stone_label, robot_paper_label, robot_points_var
    
    def __set_result_frame(self,root):
        
        result_frame = Frame( root, bg=self.RESULT_FRAME_BACKGROUNG, width=500, height=280, highlightthickness= '5', highlightbackground='blue', highlightcolor='blue' ) # 設定結果的框架

        result=StringVar() # 設定結果
        result.set('') # 設定結果
        result_label = # 設定結果
        # 放置結果  
        
        reset_btn = # 設定重置按鈕
        self.__changeOnHover(reset_btn, self.RESET_BUTTON_LIGHT_COLOR, self.RESET_BUTTON_DARK_COLOR) # 設定重置按鈕的hover效果
        # 放置重置按鈕
        
        return result_frame, result
    
    def __click_scissors(self):
        
        # 防止重複點擊
        if self.user_scissors_btn['state']!='normal' or self.user_paper_btn['state']!='normal' or self.user_stone_btn['state']!='normal': 
            return 
        else:
            self.user_scissors_btn['state']=DISABLED
                
        # 隨機產生電腦的選擇
        robot_choice = random.randint(0,2)

        if robot_choice == 0: # 剪刀
            

        elif robot_choice == 1: # 石頭
            

        else: # 布
            


        self.result_frame.place( x=self.GAME_WIDTH*0.5, y=self.GAME_HEIGHT*0.2+15, anchor='n' )

    def __click_stone(self):
        
        

    def __click_paper(self):
        
        

    def __reset_func(self):

        # 重置結果
        self.result.set('')
        self.result_frame.place_forget()

        # 重置按鈕狀態
        self.user_scissors_btn['state']=NORMAL
        self.user_paper_btn['state']=NORMAL
        self.user_stone_btn['state']=NORMAL

        # 重置電腦的選擇
        self.robot_scissors_label.place( x=140, y=400, anchor='center' )
        self.robot_stone_label.place( x=360, y=400, anchor='center' )
        self.robot_paper_label.place( x=580, y=400, anchor='center' )

        self.__update_scoreboard()

        

    def __changeOnHover(self, button, colorOnHover, colorOnLeave):
 
        # color when touching mouse
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover,foreground=colorOnLeave))
    
        # color when not touching mouse
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave, foreground=colorOnHover))

    def __update_scoreboard(self):
        
        user_score = "" # 玩家分數
        robot_score = "" # 電腦分數
    
        

        self.user_points_var.set(user_score)
        self.robot_points_var.set(robot_score)
    '''
if __name__ == '__main__':
    game = GAMING_INTERFACE()
    game.run()