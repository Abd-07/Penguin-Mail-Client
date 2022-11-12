# ***Penguin Mail*** is a **Python** based mail client which allows you to send emails

## **Project Description**

- This application as you already know, is a simple **Mail Client**
    - For now you can only send emails 
    - All data that you enter in this program is saved ONLY on your computer, because the database is local
    - To use it you will need a GMAIL account
    - ***Note : Penguin Mail is just a program which allows you to send emails from your GMAIL account, without using the GMAIL website or app***

- What I hope to implement
    - Make usernames unique 
    - Not allow 'None' as a username
    - The 'forgot username or password' feature

## **How to run this project on MacOS or Windows**

1. Install the Project from this repository
2. Open it in your code editor
3. In your Terminal
    - Write : pip install yagmail 
    - If it doesn't work try : pip3 install yagmail 
4. Open the 'main_file.py' file
5. Run it

## **The Different Sections**

1. Main Page
<img width="468" alt="Screenshot 2022-11-12 at 10 14 20 pm" src="https://user-images.githubusercontent.com/84588883/201496778-df95c584-a797-4243-a405-b6feefc7cc8e.png">
2. Account Creation Page
<img width="467" alt="Screenshot 2022-11-12 at 10 16 27 pm" src="https://user-images.githubusercontent.com/84588883/201496780-59955965-bc3f-4041-937d-c90d0003be0c.png">
3. Login Page
<img width="462" alt="Screenshot 2022-11-12 at 10 17 23 pm" src="https://user-images.githubusercontent.com/84588883/201496788-ceb1236f-0ca1-48d0-9e8b-388e9fd2d630.png">
4. Email Composing Page
<img width="612" alt="Screenshot 2022-11-12 at 10 19 41 pm" src="https://user-images.githubusercontent.com/84588883/201496796-3170d3ec-1733-47ee-8a51-0c630b55a5fd.png">

## **How to use**

- When you will run the project , the Main Page will open
    - It will have 2 buttons
        - Create account
        - Login to account
    - Obviously because you don't have an account, you will need to create one

    - In the Main Page 
        - Click on 'Create your P.M Account'
        - Write
            - Your Name
            - Your Surname
            - The username (not email address) you would like to have in this Mail Clinet
            - The password that you would like to have for this account in the Penguin Mail client
            
            - Enter your GMAIL address
            - You would probably think that you would just need to enter your GMAIL password but it's not that simple
                1. Open your browser
                2. Go to https://myaccount.google.com
                3. Sign in to your GOOGLE account
                4. Click on the 'Security' section
                5. Make sure that your GMAIL account is verified, has 2-Step Verification turned on
                5. Under "Signing in to Google", select 'App Passwords'
                6. Enter your GMAIL password
                7. Under 'Select the app and device for which you want to generate the app password.', you will select for the App 'Other'
                8. Give a name to the App. eg : 'Penguin Mail' (So if in the future you return to this section you will be able to understand which for which app did you create the password)
                9. 'Select device' is optional
                10. Click on the blue button 'Generate' 
                11. You will see a yellow box with your code (16 Characters)
                12. Copy this code
                13. Press on 'Done' at the bottom right corner
                14. Paste this code into the 'email password' feild in the Account Creation page for Penguin Mail
                15. In the Account Creation Page press 'Create Penguin Mail Account'
                
                - The source of this tutorial is this website : https://support.google.com/accounts/answer/185833?visit_id=637966989204743938-2155131695&p=InvalidSecondFactor&rd=1
        - Close the Account Creation Page
        
        - In the Main Page 
            - Click on 'Login to your P.M Account'
            - Enter 
                - Your Penguin Mail Username
                - Your Penguin Mail Password
            - Press 'login'

        - Click on the Main Page window
            - In the Menu ,You will see 'Compose'.Click on that.
                - Then, press 'New Email'
                    - Enter the details of the email you want to send
                        - The receiver
                        - The subject
                        - The body
                    - Press 'Send Email'
                    - **Congrats! You have sent your first email with Penguin Mail**

## **Team Member(s)**

- Abdulaziz Suleymanov

## **License**

- This Project has NO LICENSE, which means that the work is under exclusive copyright by default
- You can't copy, distribute, or modify my work without being at risk of take-downs, shake-downs, or litigation

Read more about the things you are ALLOWED OR NOT to do with this project : https://choosealicense.com/no-permission/ 

