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
    
    driver.find_element(By.XPATH,value='//*[@id="gigya-loginID-56269462240752180"]').send_keys("umb-1013260097")
    driver.find_element(By.XPATH,value='//*[@id="gigya-password-56383998600152700"]').send_keys("umb-1013260097")
    driver.find_element(By.XPATH,value='//*[@id="gigya-login-form"]/div[2]/div[1]/input').click()     
    
def Buscar_tareas():
    driver.implicitly_wait(5)
    #driver.find_element(By.XPATH,value='//*[@id="bundleCollapse-72d1b0f2-345e-4dec-b25d-e8304251e097-ic53a"]/material-container/div/div/div[1]/div[2]/material-tile/div/a').click()
    #driver.find_element(By.XPATH,value='//*[@id="bundleCollapse-e8cd1117-b377-43f3-adef-58bcbae83e21-ic51a"]/material-container/div/div/div[1]/div[2]/material-tile/div/a').click()
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
    if(Grammar == "Read the first sentence. Then complete the three sentences after it."):
        correctas = ["is","works","uses","works","is","makes","is","teaches","works","is","drives","takes"]
    elif(Grammar == "Complete these conversations with forms of the words do and like."):
        correctas = ["do","like","like","does","doesn't","do","like","like","do","like","don't","do","like","don't","does"]
    elif(Grammar == "Write the simple present or the present continuous forms of the verbs in parentheses."):
        correctas = ["lives","is visiting","is taking","are working","are","aren't working","are","wants","is studying","goes","likes","does not like"]
    elif(Grammar == "Watch the video. Write the correct number to answer each question."):   
        correctas = ["3","2","1","3","3"]
    elif(Grammar == "Complete the conversations. Write one or some."):   
        correctas = ["one","some","some","one","some","one"]
        inputs = driver.find_elements(By.TAG_NAME,value='input')
     
        try: 
            for contador,element in enumerate(inputs):
                element.send_keys(correctas[contador])
        except:
            check()
            check()
            iframe = driver.find_elements(By.TAG_NAME,'iframe')
            driver.switch_to.frame(iframe[0])
            inputs = driver.find_elements(By.TAG_NAME,value='input')
            for contador,element in enumerate(inputs):
                try:
                    element.send_keys(correctas[contador])
                except Exception as e:
                    pass
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
                    for _ in range(4):
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
        print(len(auxInputs))
        for element in auxInputs:
            if element.text == correctas[i]:
                try:
                    element.click()
                except:
                    body = driver.find_element(By.TAG_NAME,value='body')
                    body.click()
                    for _ in range(8):
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
    
    Grammar1 = driver.find_element(By.CLASS_NAME,value="contentblock").text[:16].strip()
    
    if Grammar1 == "A: I need a hair":
        correctas = ["Is there a","Are there any","Is there a","Are there any","Are there any","Is there a"]
    
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
                if contador == 3:
                    check()
                    check()    
                    Continue()
                    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                    driver.switch_to.frame(iframe)
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
    print(Grammar)
    if(Grammar == "Listen to the quiz. Put the words and phrases in the order you hear them."):
        correctas = ["exercise","play tennis","swim","go to the gym","go jogging","ride a bicycle","do aerobics","yoga"]
    elif(Grammar == "Watch the video. Put the restaurants in the order that Carmen and Luis see them."):
        correctas = ["Italian restaurant","Japanese restaurant","Mexican restaurant","Thai restaurant"]
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
                    for i in range(4):
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
    if(listen == "Listen to the conversation. Choose the correct place and activity for each person."):
        correctas = ["Chicago","drove to the lake","Toronto","saw a play","San Diego","went to the zoo","home","went to the movies"]
        i=0
        sleep(1)
        for j in range(4):
            inputs = driver.find_elements(By.CLASS_NAME,value="drop_area.has_drag.gap_match_gap_text_view")
            print(len(inputs))
            
            for elements in inputs:
                if elements.text == correctas[i]:
                    elements.click()
                    print(correctas[i],i)
                    i+=1
                    break

            for elements in inputs:
                if elements.text == correctas[i]:
                    elements.click()
                    print(correctas[i],i)
                    print("a",i)
                    i+=1
                    print("d",i)
                    check()
                    check()
                    Continue()
                    break
            if i<7:        
                iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                driver.switch_to.frame(iframe)
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
            if cadena == "sue has already gone ice skating.":
                cadena = "sue’s already gone ice skating."
                print("entro",cadena,sep=" , ")
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
    
    dragAndDropColumnas = driver.find_element(By.CLASS_NAME,"dds_target_view").text[:6]
    print(dragAndDropColumnas)
    if dragAndDropColumnas == "Female":
        correctas1 = ["aunt","wife","daughter","sister","niece","mother"]
        correctas2 = ["husband","brother","father","nephew","son","uncle"]
    elif(dragAndDropColumnas == "Count "):
        correctas1 = ["library","hospital","bank","theater","school","people"]
        correctas2 = ["crime","parking","pollution","noise","traffic","water"]
    elif(dragAndDropColumnas == "Types "):
        correctas1 = ["soap operas","reality shows","talk shows","game shows","sitcoms"]
        correctas2 = ["classical","rock","jazz","pop","hip-hop"]
    
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



