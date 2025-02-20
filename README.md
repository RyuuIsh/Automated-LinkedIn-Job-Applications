# Automated-LinkedIn-Job-Applications
A Python bot that automatically applies to LinkedIn job postings using Selenium.

## Features
- Automates Job Applications – Applies to LinkedIn jobs in a single click.
- Handles CAPTCHA – Pause for manual solving when needed.
- Phone Autofill – Adds phone number if required.
- Secure Login – Uses .env for credentials.
- Error Handling – Skips jobs if elements are missing.

## Tech-Stack
- Python – Core programming language
- Selenium – Automating browser actions
- dotenv – Storing credentials securely

## Setup-Instructions
### Clone the Repository
```
git clone https://github.com/yourusername/LinkedIn-Job-Apply-Bot.git
cd LinkedIn-Job-Apply-Bot
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Set up Environment Variable
Create a `.env` file and add:
```
LINKEDIN_EMAIL=your_email@gmail.com
LINKEDIN_PASSWORD=your_password
PHONE_NUMBER=your_phone_number
```
### Run the script
```
python linkedin_job_apply.py
```
### Solve CAPTCHA
When prompted, solve the CAPTCHA and press Enter.

## Future Enhancements
- Auto CAPTCHA Solver 
- Custom Keywords & Filters 
- Track Applied Jobs 

💼 Apply to jobs faster and smarter with automation




