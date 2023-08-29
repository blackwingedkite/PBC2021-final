import CMKuan_player, CMKuan_event
import pygame, os

class Game:
    __map = []
    __map_dict = {}
    __position =  None

    def __init__(self):
        self.__allsprite = pygame.sprite.Group()
        self.__clock = None
        self.__event = CMKuan_event.Event()
        self.__FPS = 40
        self.__music = None
        self.__player = None
        self.__screen = None
        self.__screen_height = 600
        self.__screen_width = 800
        self.__text_background_color = (255, 255, 255)   # white
        self.__text_color = (0, 0, 0)    # black
        self.__text_size = 20
        self.__timer = 120*40

    def check_event(self):
        player_x = self.__player.get_rect_x()
        player_y = self.__player.get_rect_y()
        event_exit, event_number = CMKuan_event.Event.reach_event(Game.__position, player_x, player_y)
        op1_clicked = False; op2_clicked = False; op3_clicked = False 
        background_color = (255, 255, 255)
        guess = False
        finish = False

        while not event_exit:
            self.update_timer()
            self.display_status()
            event_data = self.__event.display_event_text(Game.__position, event_number)
            # mouse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    op1_clicked = True if op1_t_r.collidepoint(event.pos) or op1_clicked else False
                    op2_clicked = True if op2_t_r.collidepoint(event.pos) or op2_clicked else False
                    op3_clicked = True if op3_t_r.collidepoint(event.pos) or op3_clicked else False
                    if op1_clicked: guess = op1_ans
                    if op2_clicked: guess = op2_ans
                    if op3_clicked: guess = op3_ans
                if event.type == pygame.QUIT:
                    event_exit = True
                if finish:
                    if event.type == pygame.KEYDOWN:
                        event_exit = True

            # display button
            pygame.draw.rect(self.__screen, background_color, (0, 400, self.__screen_width, 200))  # topleft(x, y, width, height)
            self.display_text_with_position(event_data[0]['question'], self.__text_size, 400, 425)
            op1_t, op1_t_r, op1_t_c, op1_t_c_r, op1_ans = self.display_button(event_data[0]['option1'], event_data[0][event_data[0]['answer']], self.__text_size, 400, 475)
            op2_t, op2_t_r, op2_t_c, op2_t_c_r, op2_ans = self.display_button(event_data[0]['option2'], event_data[0][event_data[0]['answer']], self.__text_size, 400, 525)
            op3_t, op3_t_r, op3_t_c, op3_t_c_r, op3_ans = self.display_button(event_data[0]['option3'], event_data[0][event_data[0]['answer']], self.__text_size, 400, 575)
            pygame.draw.rect(self.__screen, (255, 255, 255), op1_t_r)
            pygame.draw.rect(self.__screen, (255, 255, 255), op2_t_r)
            pygame.draw.rect(self.__screen, (255, 255, 255), op3_t_r)
            # button condition
            if op1_clicked or op2_clicked or op3_clicked:
                self.__screen.blit(op1_t_c, op1_t_c_r)
                self.__screen.blit(op2_t_c, op2_t_c_r)
                self.__screen.blit(op3_t_c, op3_t_c_r)
                if op1_ans: self.display_text_with_position(event_data[0]['explanation'], self.__text_size, 400, 425)
                if op2_ans: self.display_text_with_position(event_data[0]['explanation'], self.__text_size, 400, 425)
                if op3_ans: self.display_text_with_position(event_data[0]['explanation'], self.__text_size, 400, 425)
                finish = True
            else:
                self.__screen.blit(op1_t, op1_t_r)
                self.__screen.blit(op2_t, op2_t_r)
                self.__screen.blit(op3_t, op3_t_r)
            pygame.display.update()
        if guess: self.__player.add_point(10)

    def display_background(self):
        image_path = os.path.join("image", str(Game.__position)+".jpg")
        self.__screen.blit(Game.get_image(image_path, self.__screen_width, self.__screen_height), (0, 0))

    def display_button(self, text, answer, size, centerx, centery):
        answer = (text == answer)
        text_font = pygame.font.Font('msjh.ttf', size)
        text = text_font.render(text, True, self.__text_background_color, self.__text_color)
        text_clicked = text_font.render("Wrong", True, self.__text_color, (255, 0, 0))
        if answer: text_clicked = text_font.render("Correct", True, self.__text_color, (127, 255, 0))
        text_rect = text.get_rect()
        text_rect.centerx, text_rect.centery = centerx, centery
        text_clicked_rect = text_clicked.get_rect()
        text_clicked_rect.centerx, text_clicked_rect.centery = centerx, centery
        return text, text_rect, text_clicked, text_clicked_rect, answer

    def display_cover(self):  # 
        cover_background = Game.get_image('image\start.jpg', self.__screen_width, self.__screen_height)
        self.__screen.blit(cover_background, (0, 0))
        self.display_text_with_position("管爺每天過者0037睡覺，0939起床的日子", 28, (self.__screen_width//2), (self.__screen_height//2 - 200))
        self.display_text_with_position("卻被每天都在趕Deadline同學質疑他到底懂不懂台大校園", 28, (self.__screen_width//2), (self.__screen_height//2 - 130))
        self.display_text_with_position("否則怎麼可能那麼爽QQ", 40, (self.__screen_width//2), (self.__screen_height//2 - 60))
        self.display_text_with_position("用方向鍵操控管爺，並且蒐集散落在台大各個角落的問題", 28, (self.__screen_width//2), (self.__screen_height//2 + 40))
        self.display_text_with_position("在120秒內盡量獲得高分吧！", 28, (self.__screen_width//2), (self.__screen_height//2 + 110))
        self.display_text_with_position_color("~按任何按鍵開始~", 60, (self.__screen_width//2), (self.__screen_height//2 + 200), (255,0,0), (255, 255, 255))
        pygame.display.update()

        display_cover = True
        while display_cover:
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == event.key:
                            display_cover = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
    
    def display_ending(self):
        ending_background = Game.get_image('image\ending.jpg', self.__screen_width, self.__screen_height)
        self.__screen.blit(ending_background, (0, 0))
        self.display_text_with_position("恭喜您獲得了%d分!" % self.__player.get_point(), 50, (self.__screen_width//2), (self.__screen_height//2))
        self.display_text_with_position("按任意鍵離開", 38, (self.__screen_width//2), (self.__screen_height//2 + 100))
        pygame.display.update()

        ending = False
        while not ending:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT):
                    ending = True
                    pygame.quit()
    
    def display_event(self):
        event_flag = self.__event.display_event_flag(Game.__position)
        for item in event_flag:
            self.__screen.blit(item[0], item[1])

    def display_music(self):
        pygame.mixer.music.play(-1)

    def display_player(self):
        self.__allsprite.update()
        self.__allsprite.draw(self.__screen)

    def display_status(self):
        pink = (255, 210, 210)
        pygame.draw.rect(self.__screen, pink, (650, 0, 150, 100))  # (x, y, width, height)
        text, text_rect = self.display_text("Time: "+str(self.get_timer()//40), self.__text_size)
        text_rect.center = (725, 30)
        self.__screen.blit(text, text_rect)
        text, text_rect = self.display_text("Point: "+str(self.__player.get_point()), self.__text_size)
        text_rect.center = (725, 70)
        self.__screen.blit(text, text_rect)
    
    def display_text(self, text, size):
        text_font = pygame.font.Font('msjh.ttf', size)
        text = text_font.render(text, True, self.__text_color, self.__text_background_color)
        text_rect = text.get_rect()
        return text, text_rect
    
    def display_text_with_position(self, text, size, centerx, centery):
        text_font = pygame.font.Font('msjh.ttf', size)
        text = text_font.render(text, True, self.__text_color, self.__text_background_color)
        text_rect = text.get_rect()
        text_rect.centerx, text_rect.centery = centerx, centery
        self.__screen.blit(text, text_rect)

    def display_text_with_position_color(self, text, size, centerx, centery, t_color, t_b_color):
        text_font = pygame.font.Font('msjh.ttf', size)
        text = text_font.render(text, True, t_color, t_b_color)
        text_rect = text.get_rect()
        text_rect.centerx, text_rect.centery = centerx, centery
        self.__screen.blit(text, text_rect)

    def get_clock(self):
        return (self.__clock)
    
    def get_FPS(self):
        return (self.__FPS)

    def get_screen(self):
        return (self.__screen)
    
    def get_timer(self):
        return (self.__timer)

    def init_screen(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([self.__screen_width, self.__screen_height])
        pygame.display.set_icon(Game.get_image('image\管中閔(左).jpg', 20, 20))
        pygame.display.set_caption("管爺模擬器")

    def init_setting(self):
        pygame.mixer.init()
        self.__music = pygame.mixer.music.load('music\BGM.wav')
        pygame.mixer.music.set_volume(0.1)
        self.__clock = pygame.time.Clock()
        Game.__map.extend([[0,0,0],[0,1,0],[0,0,0]])
        Game.__position = 4
        for i in range(3):
            for j in range(3):
                num = i*3+j
                Game.__map_dict[num] = [i, j]
        self.__player = CMKuan_player.Player()
        self.__allsprite.add(self.__player)

    def update_timer(self):
        self.__clock.tick(self.__FPS)
        self.__timer -= 1
    
    @classmethod
    def get_image(cls, fileName, image_width, image_height):
        return (pygame.transform.scale(pygame.image.load(fileName), (image_width, image_height)))
    
    @classmethod
    def get_map(cls):
        return (cls.__map)
    
    @classmethod
    def get_position(cls):
        return (cls.__position)

    @staticmethod
    def update_class_map(position):
        pos_x, pos_y = Game.__map_dict[Game.__position]
        Game.__map[pos_x][pos_y] = 0
        pos_x, pos_y = Game.__map_dict[position]
        Game.__map[pos_x][pos_y] = 1
        Game.__position = position