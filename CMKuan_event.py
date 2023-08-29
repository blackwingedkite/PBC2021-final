import json, pygame

class Event:
    __posMatrix = []
    __reachMatrix = []

    def __init__(self):
        self.__event_height = 60
        self.__event_width = 60
        self.init_setting()
    
    def init_setting(self):
        Event.__posMatrix.extend([
            [[100, 264],[666, 333],[398, 431]], # pos0
            [[444, 122],[623, 94],[199, 331]],  # pos1
            [[543, 126],[479, 264],[333, 333]], # pos2
            [[444, 444],[200, 100],[277, 121]], # pos3
            [[555, 115],[300, 404],[431, 232]], # pos4
            [[112, 112],[455, 205],[387, 343]], # pos5
            [[334, 334],[511, 276],[101, 454]], # pos6
            [[443, 443],[217, 123],[321, 234]], # pos7
            [[554, 554],[160, 431],[345, 185]], # pos8
        ])
        for i in range(9):
            Event.__reachMatrix.append([1, 1, 1])

    def display_event_flag(self, position):
        eventList = []
        counter = 0
        for item in Event.__posMatrix[position]:
            image = pygame.Surface((self.__event_width, self.__event_height))
            event_flag = 'image\Kizuna.png'
            if Event.__reachMatrix[position][counter] == 1:
                event_flag = 'image\Peko.png'
            image = pygame.transform.scale(Event.get_image(event_flag, self.__event_width, self.__event_height), (self.__event_width, self.__event_height))
            image_rect = image.get_rect()
            image_rect.centerx, image_rect.centery = item[0], item[1]
            eventList.append([image, image_rect])
            counter += 1
        return eventList

    def display_event_text(self, position, question):
        eventlist = self.searchFile(position)
        return eventlist[question]
    
    def searchFile(self, position):
        with open('data.json', encoding='UTF-8') as json_file:
            data = json.load(json_file)
            return data[str(position)]

    @classmethod
    def get_image(cls, fileName, image_width, image_height):
        return (pygame.transform.scale(pygame.image.load(fileName), (image_width, image_height)))
    
    @classmethod
    def reach_event(cls, position, player_cx, player_cy):
        event_exit = True
        event_number = 0
        counter = 0
        for item in Event.__posMatrix[position]:
            if (player_cx > (item[0]-60)) and (player_cx < (item[0]+60)) and (player_cy > (item[1]-60)) and (player_cy < (item[1]+60)):
                if Event.__reachMatrix[position][counter] == 1:
                    Event.__reachMatrix[position][counter] = 0
                    event_exit = False
                    event_number = counter
            counter += 1
        return event_exit, event_number