from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException,ElementClickInterceptedException,NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def check():
    driver.switch_to.default_content()
    sleep(1)
    driver.find_element(By.XPATH,value='/html/body/app/div/learner/activity-view/div/div/main/div/div[2]/div/a[1]').click()

def Continue():
    driver.switch_to.default_content()
    sleep(1)
    try:
        driver.find_element(By.XPATH,"/html/body/app/div/learner/activity-view/div/div/main/div/div[1]/result-screen/div/div/div/div/div/div/div[3]/p[1]/a").click()
    except:
        pass

def Iniciar_Sesion():   
    driver.find_element(By.XPATH,value='//*[@id="onboarding-header-login-btn"]').click()
    
    driver.find_element(By.XPATH,value='//*[@id="gigya-loginID-56269462240752180"]').send_keys("umb-1012917841")
    driver.find_element(By.XPATH,value='//*[@id="gigya-password-56383998600152700"]').send_keys("umb-1012917841")
    driver.find_element(By.XPATH,value='//*[@id="gigya-login-form"]/div[2]/div[1]/input').click()     
    
def Buscar_tareas():
    driver.implicitly_wait(5)
    #driver.find_element(By.XPATH,value='//*[@id="bundleCollapse-user_cd50ac64eba3401a992a5e6e2617680e-ic2"]/material-container/div/div/div[1]/div[2]/material-tile/div/a').click()
    driver.find_element(By.CLASS_NAME,value='no-decoration.tile-section-1.d-flex.align-items-center').click()

    sleep(3)
    
    prueba = driver.find_elements(By.TAG_NAME,value='a')
    #AGREGAR LA FUNCION DE ELEGIR QUE MODULO
    
    x = input("joce")
    # for element in prueba:
    #  qid_attribute = element.get_attribute("qid")
    #  if qid_attribute == "productView-5-7-1-4":
    #  #if qid_attribute == "productView-5-0-1-2":
    #         element.click()
    #         break
    
    sleep(3)
    
def Tarea_Escribir():
    
    correctas = []

    Grammar = driver.find_element(By.CLASS_NAME,value="rubricWrap").text[16::].strip()
    
    print(Grammar)
    
    if Grammar == "Watch the video. What are the people going to do? Put the activities in the order that the people talk about them. Type the numbers 1-7 in the blanks.":
        correctas = ["2","6","7","5","3","1","4"]
    elif Grammar == "Complete the conversations with the correct form of be going to and the verbs in parentheses.":
        correctas = ["are","going to do","am going to go","are","going to work","am going to work","is","going to do","is going to play",
                     "are","going to celebrate","am going to meet","are","going to go","are going to travel",
                     "is","going to invite","is going to invite","are","going to take","are going to study",
                     "are","going to order","am going to order"]
    elif Grammar == "Watch the video. Number the events in the correct order.":
        correctas = ["3","2","1","6","5","4"]
    elif Grammar == "Listen to the conversations. Number each person's activities in order from 1 to 4.":
        correctas = ["3","1","4","2","2","4","3","1","1","3","2","4"]
    elif Grammar == "What's wrong with the person? Complete the sentence with has and the correct word from the list.":
        correctas = ["has a toothache","has a sore throat","has an earache","has a stomachache","has a headache"
                     ,"has a backache"]
        
        inputs = driver.find_elements(By.TAG_NAME,value='input')
     
        for contador,element in enumerate(inputs):
            try: 
                element.send_keys(correctas[contador])
            except ElementNotInteractableException:
                check()
                check()
                iframe = driver.find_elements(By.TAG_NAME,'iframe')
                driver.switch_to.frame(iframe[0])
                inputs = driver.find_elements(By.TAG_NAME,value='input')[contador]
                inputs.send_keys(correctas[contador])
        check()
        check()
        Continue()
        return
    elif Grammar == "Watch the video. Number the activities in the correct order.":
        correctas = ["5","6","3","1","2","4"]
    elif Grammar == "Complete the conversations with like to, love to, or want to.":
        correctas = ["want to","like to","like to","like to","like to","love to","want to","like to","like to","want to",
                     "want to","like to"]
        
        inputs = driver.find_elements(By.TAG_NAME,value='input')
     
        for contador,element in enumerate(inputs):
            try: 
                element.send_keys(correctas[contador])
            except ElementNotInteractableException:
                check()
                check()
                iframe = driver.find_elements(By.TAG_NAME,'iframe')
                driver.switch_to.frame(iframe[0])
                inputs = driver.find_elements(By.TAG_NAME,value='input')[contador]
                inputs.send_keys(correctas[contador])
        check()
        check()
        Continue()
        return
    elif Grammar == "Kate called her friend yesterday. Where was she? Complete the conversation with the correct preposition and word from the box.":
        correctas = ["at the mall","in bed","on vacation","in the hospital","at the library","at work"]
        
        inputs = driver.find_elements(By.TAG_NAME,value='input')
     
        for contador,element in enumerate(inputs):
            try: 
                element.send_keys(correctas[contador])
            except ElementNotInteractableException:
                check()
                check()
                iframe = driver.find_elements(By.TAG_NAME,'iframe')
                driver.switch_to.frame(iframe[0])
                inputs = driver.find_elements(By.TAG_NAME,value='input')[contador]
                inputs.send_keys(correctas[contador])
        check()
        check()
        Continue()
        return
    else: 
        driver.execute_script("window.open(window.location.href);")
        sleep(1)
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        inputs = driver.find_elements(By.TAG_NAME,value='input')
        try:        
            for element in inputs:
                element.send_keys("1")
        except ElementNotInteractableException:
            pass
        
        check()
            
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        sleep(1)
        try:
            driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
        except:
            pass
        
        inputs = driver.find_elements(By.CSS_SELECTOR,value='div.check.wrong.has-feedback') 
        correctas = []

        body = driver.find_element(By.TAG_NAME,value='body')
        sleep(1)
        
        for element in inputs:
            try:
                element.click()
            except ElementClickInterceptedException:
                body.click()
                body.send_keys(Keys.HOME)
                try:
                    driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
                except:
                    pass
            finally:
                sleep(0.15)
                try:
                    element.click()
                except:
                    body.click()
                    for _ in range(6):
                        body.send_keys(Keys.ARROW_DOWN)
                    sleep(1)
                    element.click()
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').text.split('\n')
                temp = temp[2]      
            correctas.append(temp)

        driver.close()
        
        sleep(1)
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])

        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
    inputs = driver.find_elements(By.TAG_NAME,value='input')

    try:        
        for contador,element in enumerate(inputs):
            element.send_keys(correctas[contador])
    except:
        pass
    
    check()
    check()
    Continue()
    
def Tarea_Seleccionar():
    
    correctas = []
    
    Grammar = driver.find_element(By.CLASS_NAME,value="rubricWrap").text[16::].strip()
    Grammar1 = driver.find_element(By.CLASS_NAME,value="contentblock").text[:16].strip()
    print(Grammar1)
    if Grammar == "Read the story. Choose True or False.":
        correctas = ["False","True","False","False","True"]
    elif Grammar1 == "1. Ray's Health":
        correctas = ["True","True","True","True","False","False"]
    elif Grammar1 == "1. Olivia was su":
        correctas = ["True","False","False","True","False","True","False"]
    elif Grammar1 == "1. People in Arg":
        correctas = ["True","True","True","False","False","True"]
    elif Grammar1 == "1. Sylvia came t":
        correctas = ["True","False","True","True","False","True","False","False"]
    elif Grammar1 == "1. At the beginn":
        correctas = ["He wants to hear Abby's story.","I'm listening.","She likes Greg, but she doesn't like sports.",
                     "Sunday","when he was having lunch","She's very busy."]
    else:
        driver.execute_script("window.open(window.location.href);")
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        inputs = driver.find_elements(By.CLASS_NAME,value='input-radio')
        body = driver.find_element(By.TAG_NAME,value='body')
        a=True
        while(a):
            try:        
                for element in inputs:
                    sleep(0.5)
                    element.click()
            except ElementClickInterceptedException:
                body.click()
                for _ in range(8):
                    body.send_keys(Keys.ARROW_DOWN)   
                sleep(1)
                element.click()
            try:
                check()
                a = False
            except ElementNotInteractableException:
                print("Reintentando activdad")
                body.click()
                body.send_keys(Keys.HOME)
                
            
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        body = driver.find_element(By.TAG_NAME,value='body')
        body.click()
        body.send_keys(Keys.HOME)
        
        sleep(1)
        try:
            driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
        except:
            pass

        correctas = []

        body = driver.find_element(By.TAG_NAME,value='body')
        inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')
        for element in inputs:
            try:
                element.click() 
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                if temp == "":
                    aux = element.find_element(By.XPATH,value='..').find_element(By.TAG_NAME,value="label").text
                    temp = aux
                sleep(0.25)
            except ElementClickInterceptedException:
                body = driver.find_element(By.TAG_NAME,value='body')
                body.click()
                for _ in range(8):
                    body.send_keys(Keys.ARROW_DOWN)   
                sleep(1)
                element.click()
                sleep(1)
                element.click()    
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                if temp == "":
                    aux = element.find_element(By.XPATH,value='..').find_element(By.TAG_NAME,value="label").text
                    temp = aux
            except:
                pass
            correctas.append(temp)
            
        driver.close()
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
    
    inputs = driver.find_elements(By.CLASS_NAME,value='choice_interaction.algn-ver.has-input')
    i=0
    
    for input in inputs:
        auxInputs = input.find_elements(By.CLASS_NAME,value='is-radiobutton-choice-text')
        for element in auxInputs:
            if element.text == correctas[i]:
                try:
                    element.click()
                except:
                    body = driver.find_element(By.TAG_NAME,value='body')
                    for _ in range(6):
                        body.send_keys(Keys.ARROW_DOWN)   
                    sleep(1)
                    element.click()
                finally:
                    i+=1
                    break                    
                    
    check()
    check()
    Continue()
       
def Tarea_desplegable():
    
    correctas = []
    
    Grammar = driver.find_element(By.CLASS_NAME,value="contentblock").text[16:42].strip()
    Grammar1 = driver.find_element(By.CLASS_NAME,value="contentblock").text[:16].strip()
    listen = driver.find_element(By.CLASS_NAME,value="rubricWrap").text[16::].strip()
    
    print("Listen: ",listen)
    print(Grammar,Grammar1,sep=" - ")
    
    if Grammar1 == "1. Don’s younger":
        correctas = ["paints animal portraits","acts in a theater","every morning","every morning","processes payments","cakes and pastries"]
    elif Grammar == "ildren want to skip school":
        correctas = ['Bullying', 'Graffiti', 'inadequate health care', 'stray animals', 'noise pollution', 'street crime', 'The lack of child care']
    elif Grammar == "to grow enough food for ev":
        correctas = ["will have found","will know","won't allow","will be trying","will have been","will have moved","will be","will last",
                     "won't be living","will have"]
        
        inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
          
        for contador,elements in enumerate(inputs):
            try:
                elements.click()
            except:
                check()
                check()
                Continue()
                iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                driver.switch_to.frame(iframe)  
                elements.click()
            finally:
                aux = elements.find_elements(By.TAG_NAME,value='li')
                for element in aux:
                    aux1 = element.text.replace("’","'")
                    print(aux1,correctas[contador],sep= " - ")
                    if aux1 == correctas[contador]:
                        element.click()
            
        check()
        check()
        Continue()
        return
    elif Grammar[:-5] == "ng to do this weekend": 
        correctas = ["are you","Where are you","What are you","Is","Where is it","when is it","is Bob","are you going to"]  
        
        inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
        for contador,elements in enumerate(inputs):
            try:
                elements.click()
            except:
                check()
                check()
                Continue()
                iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                driver.switch_to.frame(iframe)  
                elements.click()
            finally:
                try:
                    aux = elements.find_elements(By.TAG_NAME,value='li')
                except NoSuchElementException:
                    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                    driver.switch_to.frame(iframe)  
                    body = driver.find_element(By.TAG_NAME,value='body')
                    for _ in range(8):
                        body.send_keys(Keys.ARROW_DOWN)
                        sleep(0.25)
                    inputAux = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
                    print(len(inputAux))
                    aux = inputAux[7].find_elements(By.TAG_NAME,value='li')
                    for element in aux:
                        print(aux1,correctas[7],sep= " - ")
                        if aux1 == correctas[7]:
                            element.click()
                    
                for element in aux:
                    aux1 = element.text.replace("’","'")
                    print(aux1,correctas[contador],sep= " - ")
                    if aux1 == correctas[contador]:
                        element.click()
                        
        check()
        check()
        Continue()
        return
    elif listen == "Listen to someone leave a message for Kate. Choose the correct answers.":
        correctas = ["Don","see a movie","4 P.M.","Bill","dinner","work late","Howard","English","home"]  
        
        inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
        for contador,elements in enumerate(inputs):
            try:
                elements.click()
            except:
                check()
                check()
                Continue()
                iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                driver.switch_to.frame(iframe)  
                elements.click()
            finally:
                try:
                    aux = elements.find_elements(By.TAG_NAME,value='li')
                except NoSuchElementException:
                    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                    driver.switch_to.frame(iframe)  
                    body = driver.find_element(By.TAG_NAME,value='body')
                    for _ in range(8):
                        body.send_keys(Keys.ARROW_DOWN)
                        sleep(0.25)
                    inputAux = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
                    print(len(inputAux))
                    aux = inputAux[7].find_elements(By.TAG_NAME,value='li')
                    for element in aux:
                        print(aux1,correctas[7],sep= " - ")
                        if aux1 == correctas[7]:
                            element.click()
                    
                for element in aux:
                    aux1 = element.text.replace("’","'")
                    print(aux1,correctas[contador],sep= " - ")
                    if aux1 == correctas[contador]:
                        element.click()
                        
        check()
        check()
        Continue()
        return

    else: 
        driver.execute_script("window.open(window.location.href);")
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)          
        
        inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
        body = driver.find_element(By.TAG_NAME,value='body')

        for elements in inputs:
            try:    
                elements.click()
                aux = elements.find_element(By.TAG_NAME,value='li').click()
            except:
                body.click()
                for _ in range(8):
                    body.send_keys(Keys.ARROW_DOWN)   
                sleep(1)
                elements.click()
                aux = elements.find_element(By.TAG_NAME,value='li').click()

        check()
            
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        body = driver.find_element(By.TAG_NAME,value='body')
        body.click()
        body.send_keys(Keys.HOME)
        
        sleep(1)
        driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()

        correctas = []

        inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')
        for element in inputs:
            try:
                try:
                    element.click()
                except:
                    body.click()
                    for _ in range(2):
                        body.send_keys(Keys.ARROW_UP)   
                sleep(1) 
                element.click()
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                if temp == "":
                    aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="label.drop-label").text
                    temp = aux
                sleep(0.25)
            except ElementClickInterceptedException:
                try:
                    driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
                except:
                    pass
                body = driver.find_element(By.TAG_NAME,value='body')
                body.click()
                for _ in range(8):
                    body.send_keys(Keys.ARROW_DOWN)   
                sleep(1)
                try:
                    element.click()
                except:
                    body.click()
                    for _ in range(2):
                        body.send_keys(Keys.ARROW_UP)   
                    sleep(1)
                    element.click()
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                if temp == "":
                    aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="label.drop-label").text
                    temp = aux
                    
            except:
                pass
            correctas.append(temp)
            
        driver.close()
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])

        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
     
    print(correctas)   
    inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
    contador=0
    
    body = driver.find_element(By.TAG_NAME,value='body')
    
    for elements in inputs:
        try:   
            elements.click()
        except:
            body.click()
            for _ in range(8):
                body.send_keys(Keys.ARROW_DOWN)   
            sleep(2)
            elements.click()
    
        finally:
            aux = elements.find_elements(By.TAG_NAME,value='li')
            for element in aux:
                if element.text == correctas[contador]:
                    element.click()
            contador+=1
            
    check()
    check()    
    Continue()
    
def Tarea_DragAndDrop():
    
    correctas = []

    Grammar = driver.find_element(By.CLASS_NAME,value="rubricWrap").text[16::].strip()
    Grammar1 = driver.find_element(By.CLASS_NAME,value="contentblock").text[:7].strip()
    print(Grammar,Grammar1,sep=" - ")
    
    if(Grammar1 == "1. Luca"):
        correctas = ["fix your car","play the violin","tell good jokes","ride a horse","snowboard","edit a video",
                     "do a handstand","play chess"]
    else:
        driver.execute_script("window.open(window.location.href);")
        sleep(2)
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)          
        
        inputs = driver.find_elements(By.CLASS_NAME,value="drop_area.has_drag.gap_match_gap_text_view")
        
        sleep(1)
        
        for elements in inputs:
            elements.click()
            
        check()
        sleep(1)
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        sleep(1)
        driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
        
        correctas = []

        body = driver.find_element(By.TAG_NAME,value='body')
        inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')

        for element in inputs:
            try:
                element.click() 
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                if temp == "":
                    aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="content").text
                    temp = aux
                sleep(0.25)
            except ElementClickInterceptedException:
                try:
                    driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
                except:
                    pass
                sleep(0.25)
                try:
                  element.click()    
                except ElementClickInterceptedException:
                    body.click()
                    for i in range(6):
                     body.send_keys(Keys.ARROW_DOWN)
                    sleep(1)
                    element.click()
                finally:
                    temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                    if temp == "":
                        aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="content").text
                        temp = aux
            except NoSuchElementException:
                pass
            correctas.append(temp)
            
        print(correctas)  
        driver.close()
        
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])

        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
    
    inputs = driver.find_elements(By.CLASS_NAME,'drop_area.gap_match_gap_text_view.has_drag')    
    
    contador=0
    while(contador < len(correctas)):    
        for elements in inputs:
            aux = elements.text.strip()
            try:
                if aux.lower() == correctas[contador].lower():
                    elements.click()
                    contador+=1
            except:
                break
    check()
    check()
    Continue()
        
def Tarea_DragAndDrop2():
    
    correctas = []

    listen = driver.find_element(By.CLASS_NAME,value="rubricWrap").text[16::].strip()
    Grammar1 = driver.find_element(By.CLASS_NAME,value="contentblock").text[:7].strip()
    
    print(listen,Grammar1,sep=" - ")
    
    if listen == "Complete the sentence with the correct remedy. Use the picture.":
        correctas = ["aspirin","eye drops","cough syrup","an antacid","cold medicine","an ice pack"]
           
        inputs = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
        i=0
        
        for elemets in inputs:
            element = elemets.find_elements(By.CLASS_NAME,value="drop_area.gap_match_gap_text_view.has_drag")
            for elements in element:
                print(elements.text,correctas[i],sep=" , ")
                if elements.text == correctas[i]:
                    elements.click()
                    i+=1
                    check()
                    check()
                    Continue()
                    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                    driver.switch_to.frame(iframe)
                    break
    elif Grammar1 == "Sofia:":
        correctas = ["Did","have","had","rode","felt","came","Did","go","didn't","watched","made",
                     "Did","have","did","went","ate","took","saw","Did","take","took","bought"]
        
        inputs = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
        i=0
        aux = True
        
        for elemets in inputs:
            aux=True
            while aux:
                element = elemets.find_elements(By.CLASS_NAME,value="drop_area.gap_match_gap_text_view.has_drag")
                for elements in element:
                    print(elements.text,correctas[i],sep=" , ")
                    if elements.text == correctas[i]:
                        elements.click()
                        i+=1
                        if i == 11:
                            aux=False
                            check()
                            check()
                            Continue()
                            iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                            driver.switch_to.frame(iframe)
                            break
                        elif i > 20:
                            aux = False
        check()
        check()
        Continue()
                    
    else:
        driver.execute_script("window.open(window.location.href);")
        sleep(1)
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
        
        inputs = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
        
        correctas = []

        for i in range(len(inputs)):
            zone = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
            zone = zone[i].find_elements(By.CLASS_NAME,'drag_element.gap_match_drag.image-between-text')
            
            opciones = []
            for elements in zone:
                opcion = elements.find_element(By.CLASS_NAME,'content').text
                opcion = opcion.lower()
                opciones.append(opcion)
            
            for i,elements in enumerate(zone,1):
                if i%2==0:
                    elements.click()
            check()
            
            iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
            driver.switch_to.frame(iframe)
            
            try:
                driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
            except:
                pass

            cadena = driver.find_element(By.CLASS_NAME, 'ui-draggable.ui-draggable-handle').find_element(By.TAG_NAME, 'p').text[26:].strip()   
            cadena = cadena.lower()
                
            if "," in opciones:   
                cadena = cadena.replace(",", " ,")
            
            if "'" in cadena:
                cadena = cadena.replace("'", "’")
                
            opciones = [element.replace("'", "’") for element in opciones]
            
            print(cadena)
            print(opciones)
            
            N_cadena = [] 
            palabras = cadena.split()
            
            aux = ""
            
            for palabra in palabras:
                aux += palabra + " "    

                if aux.strip() in opciones:
                    opciones.remove(aux.strip())
                    N_cadena.append(aux.strip())
                    aux = ""

            if aux.strip():
                N_cadena.append(aux.strip()[:-1])

            for respuestas in N_cadena:
                correctas.append(respuestas)

            check()
            iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
            driver.switch_to.frame(iframe)
        driver.close()
        
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])

        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
        
        inputs = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")

        contador,contadoraux = 0,0
        print(correctas)
        
        try:
            if correctas[7] == "sometimes have a sandwich for lunch":
                correctas = ['they', 'usually', 'have', 'chicken', 'for', 'dinner', 'i', 'often', 'have', 'a', 'sandwich', 'for', 'lunch', 'he', 'always', 'eats', 'breakfast', 'at', 'home', 'she', 'never', 'has', 'any', 'snacks', 'i',
                             'hardly ever', 'have', 'pasta', 'for', 'dinner']
            elif correctas[7] == "supermarket is next to the chinese restaurant":
                correctas = ['the', 'bookstore', 'is', 'on', 'second', 'street', 'the supermarket is','next', 'to', 'the', 'chinese',
                             'restaurant','the', 'department', 'store', 'is', 'on', 'brown', 'street','the gas',
                             'station is','behind', 'the','mexican','restaurant', 'the hotel is','across','from','the','english','school',
                             'the', 'drugstore', 'is', 'on', 'harris', 'street', 'the chinese restaurant is','near','the','post','office',
                             'the','post','office','is','on','brown','street']
            elif correctas[4] == "gabriel garcía márquez":
                correctas = ['marie curie', 'was', 'a', 'scientist', 'gabriel garcía márquez', 'was', 'born', 'in',
                             'colombia', 'maya angelou', 'wrote', 'a', 'famous', 'book', 'michelle yeoh', 'was', 'in', 
                             'the', 'movie', '"supercop."', 'grace kelly', 'was', 'born', 'in 1929', 'and', 'died', 'in 1982',
                             'salvador dalí', 'was', 'a', 'spanish', 'artist']
        except:
            pass
        
        for i in range(len(inputs)):
            a=True
            zone = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
            zone = zone[i].find_elements(By.CLASS_NAME,'drag_element.gap_match_drag.image-between-text')
            while(a):    
                for i,elements in enumerate(zone,1):
                    try:
                        label = elements.find_element(By.CLASS_NAME,'content').text
                        label = label.lower()
                        if "'" in label:
                            label = label.replace("'", "’")
                    except:
                        pass
                    try:
                        print(label,correctas[contador],sep=" , ")
                        if label == correctas[contador]:
                            elements.click()
                            contador+=1
                            contadoraux+=1
                            if contadoraux == len(zone)/2:
                                contadoraux=0
                                check()
                                check()
                                a = False
                                iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                                driver.switch_to.frame(iframe)  
                    except IndexError:
                        Continue()
def checkbox():
    
    correctas = []

    listen = driver.find_element(By.CLASS_NAME,value="rubricWrap").text[16::].strip()
    
    print(listen)
    
    if listen == "Watch the video. What does each person order for brunch? Choose the correct answers.":
        correctas = ["Man 1","Woman","Man 2","Woman",["Boy","Man 1"],"Boy","Woman","Man 1"]
        
    elif listen == "Listen to Danielle talk to Lei. What sports do their children play? Choose the correct answers.":
        correctas = ["Tao",["Tao","Ying"],"Tao","Amanda",["Amanda","Ying"]]
        
    elif listen == "Listen to the conversations. What does the pharmacist tell the people about the medications? Choose the correct answers. Sometimes more than one answer is possible.":
        correctas = [["Use it when your back hurts.","Don't let children use it."],["Don't take any other medications with the pills.","Take the pill with food and drink a lot of water."]
                     ,["Give it to him two times a day.","Make an appointment to see a doctor."],"Put three drops in each eye."]
    elif listen == "Listen to Rima and Dan talk about their plans for tomorrow. Who is going to go to each place? Choose the correct answers. More than one answer may be possible.":
        correctas = ["Rima","Dan",["Rima","Dan"],"Dan","Rima"]  
    elif listen == "Read the blog. Choose the correct answers. There may be more than one correct answer.":
        correctas = ["River Park","Friday","with his roommates.","Yellow Star City Center",["Saturday","Sunday"],
                     "with his brother.","Mission Park",["Friday","Saturday","Sunday"],"alone."]
    else:
    
        driver.execute_script("window.open(window.location.href);")
        sleep(1)
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
        
        inputs = driver.find_elements(By.CLASS_NAME,value="is-checkbox-choice-text")
        body = driver.find_element(By.TAG_NAME,value='body')
        
        for element in inputs:
            try:
                element.click()
            except (ElementClickInterceptedException,ElementNotInteractableException) as e: 
                body.click()
                for _ in range(8):
                    body.send_keys(Keys.ARROW_DOWN)
                    sleep(0.25)
                element.click()
                print(element.text)

        check()
            
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
        
        sleep(1)
        try:
            driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
        except:
            pass
        
        correctasAux = []
        body = driver.find_element(By.TAG_NAME,value='body')
        
        inputs = driver.find_elements(By.CLASS_NAME,value='choice_interaction.algn-ver.has-input')

        body.click()
        body.send_keys(Keys.HOME)
        sleep(1)
        
        for element in inputs:
            try:
                elements = element.find_element(By.CLASS_NAME,value='check.wrong.has-feedback')
                elements.click()
                respuesta = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
            except NoSuchElementException as e:
                elements = element.find_element(By.CLASS_NAME,value='check.correct.has-feedback')
                elements.click()
                respuesta = elements.find_element(By.XPATH,value='..').text
            except ElementClickInterceptedException:
                body.click()
                for _ in range(6):
                    body.send_keys(Keys.ARROW_DOWN)
                sleep(1)
                elements = element.find_element(By.CLASS_NAME,value='check.wrong.has-feedback')
                elements.click()
                respuesta = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                
            correctasAux.append(respuesta)
            sleep(0.25)
        
        correctas = []
        aux = ""
        for i in correctasAux:
            aux = i.replace(':\n', '').replace('\n', ',')
            if ',' in aux:
                correctas.append(aux.split(','))
            else:
                correctas.append(aux)     
        print(correctas)
        
        driver.close()
        
        ventanas = driver.window_handles 
        driver.switch_to.window(ventanas[0])

        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
        
    inputs = driver.find_elements(By.CLASS_NAME,value="choice_interaction.algn-ver.has-input")
    print(len(inputs))
    i,aux=0,0
    
    body = driver.find_element(By.TAG_NAME,value='body')
    
    for element in inputs:
        elements = element.find_elements(By.CLASS_NAME,value="is-checkbox-choice-text")
        for opciones in elements:
            print(opciones.text,correctas[i],sep=" , ")
            if opciones.text in correctas[i]:
                try:
                    opciones.click()
                except (ElementClickInterceptedException,ElementClickInterceptedException) as e:
                    for _ in range(6):
                        body.send_keys(Keys.ARROW_DOWN)
                        sleep(0.25)
                    opciones.click()      
                aux+=1
                print("aux: ",aux)
                print("len: ",len(correctas[i]))
                if isinstance(correctas[i],list):
                    if aux == len(correctas[i]):
                        i+=1
                        aux=0
                        print("i: ",i)
                        break
                else:
                    i+=1
                    aux=0
                    print("i: ",i)
                    break
                sleep(0.5)
    check()
    check()
    Continue()

def DragAndDropColumnas():
    correctas = []
    print("seleccionar columnas")
    
    dragAndDropColumnas = driver.find_element(By.CLASS_NAME,"dds_target_view").text[:-5]
    grammar = driver.find_element(By.CLASS_NAME,"rubricWrap").text[16::].strip()
    
    print(dragAndDropColumnas,grammar,sep=" - ")
    if grammar == "Put the words in the correct category. There are four words in each category.":
        correctas1 = ["cooked","shopped","watched","worked"]
        correctas2 = ["cleaned","exercised","opened","stayed"]
        correctas3 = ["invited","painted","visited","waited"]
        
        dragItem = driver.find_elements(By.CLASS_NAME,"drag_item.os-sorting-element.image-between-text")
    
        for element in dragItem:
            if element.text in correctas1:
                element.click()

        for element in dragItem:
            if element.text in correctas2:
                element.click()
                
        for element in dragItem:
            if element.text in correctas3:
                element.click()
                
        check()
        check()
        Continue()
    elif dragAndDropColumnas == "go":
        correctas1 = ["bike riding","hiking","ice-skating","snowboarding","swimming"]
        correctas2 = ["baseball","basketball","golf","hockey","soccer","tennis","volleyball"]
    
    dragItem = driver.find_elements(By.CLASS_NAME,"drag_item.os-sorting-element.image-between-text")
    
    for element in dragItem:
        if element.text in correctas1:
            element.click()

    for element in dragItem:
        if element.text in correctas2:
            element.click()
            
    check()
    check()
    Continue()

def Inicio():
    driver.get("https://www.cambridgeone.org")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    Iniciar_Sesion()
    Buscar_tareas()

def Tareas():  
             
    if (inputs := driver.find_elements(By.CLASS_NAME, "input-text.has-input")):
        Tarea_Escribir() 
        
    elif(dragAndDrop := driver.find_elements(By.CLASS_NAME,"pool.ui-droppable")) and len(dragAndDrop) == 1: 
        print("draganddrop")
        Tarea_DragAndDrop()
        
    elif(dragAndDrop2 := driver.find_elements(By.CLASS_NAME,"pool.ui-droppable")) and len(dragAndDrop2) > 1: 
        print("draganddrop2")
        Tarea_DragAndDrop2()
        #prueba = input("darganddrop")
            
    elif(desplegar := driver.find_elements(By.CLASS_NAME,"rich-dropdown")) and len(desplegar)>= 1:
        print("desplegable")
        Tarea_desplegable()
          
    elif(Checkbox := driver.find_elements(By.CLASS_NAME,"input-checkbox")): 
        print("checkbox")
        checkbox();
            
    elif(seleccionar := driver.find_elements(By.CLASS_NAME,"contentblock.alignment-vertical")) and len(seleccionar) == 1: 
        print("seleccionar")
        Tarea_Seleccionar()    
            
    elif(seleccionar2 := driver.find_elements(By.CLASS_NAME,"contentblock.alignment-vertical")) and len(seleccionar2) > 1: 
        print("seleccionar2")
        prueba = input("Seleccionar2")
            
    elif(dragAndDropColumnas := driver.find_elements(By.CLASS_NAME,"drop_zone.ui-droppable")): 
            DragAndDropColumnas()    
    else:
        print("no entro a ninguna")
            

Inicio()
contador = 0
while(True):
    try:
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
    except IndexError as e:
        print("Error iframe incorrecto",e)
        pass
    contador+=1
    print(f"it : {contador}")
    try:
        Tareas()    
    except Exception as e:
        print(e)
        input("error del try catch inicial")
    sleep(1)



