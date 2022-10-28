# Testing

[Return to README.md](README.md)

- [Bugs and Fixes During the Development Process](#bugs-and-fixes-during-the-development-process)
- [Wave Aim Accessibility checker:](#wave-aim-accessibility-checker)
- [Lighthouse](#lighthouse)
  - [Mobile](#mobile)
  - [Desktop](#desktop)
- [Validators](#validators)
  - [HTML](#html)
  - [CSS](#css)
  - [Javascript](#javascript)
  - [Python](#python)
- [User Stories](#user-stories)

## Bugs and Fixes During the Development Process
- Messages
    - Issue - Messages were not being removed automatically.
    - Cause - The messages were set to display, but not set to close without user intervention.
    - Solution - I added a timeout script to the base file which would close the message after 3 seconds.
- Images
    - Issue - Images weren't displaying.
    - Cause - The links for the images were not correct, and so were unable to display anything from Cloudinary.
    - Solution - I changed the image links to cloudinary urls.
- Weight Tracker
    - Issue - Data wasn't pulling through to the chart on the weight tracker.
    - Cause - I hadn't converted the weight stats to an integer or the dates to strings.
    - Solution - I added an integer specifier to my health tracker view for my serialized weight list and a string specifier for my serialized date list.
- Delete Entry
    - Issue - Original deletion functionality wasn't working when I had modals set up to pop up when the user clicked the delete button. Whichever delete button was used, the same data was deleted.
    - Cause - The modal IDs were conflicting with the entry IDs, so it was deleting the same entry each time.
    - Solution - I changed approach from using modals to delete to using a DeleteView from django's generic views.
- SEO
    - Issue - SEO score was quite low.
    - Cause - I had forgotten the description, author and keywords information for the meta tag and SEO's weren't picking up 'read more' on my article links.
    - Solution - I added this information in to the meta tag and amended the links to read 'learn more'.
- Emails
    - Issue - Emails were not sending outside of the development environment.
    - Cause - I had not configured my config vars on Heroku to include my EMAIL_HOST_USER and EMAIL_HOST_PASSWORD variables.
    - Solution - I added these into Heroku and the emails began sending and the error message stopped showing.
- Health Hub
    - Issue - The data in the table was showing the most recent data by date only. If the user had added multiple stats on the same day, it would only display the first set of stats on that day. It should have shown the most recent set of stats in time.
    - Cause - The date field was set up as a datefield in the healthstats model.
    - Solution - The date field was changed to a datetime field instead, this fixed the issue.

## Accessibility

## Lighthouse

### Desktop

![Lighthouse Desktop Score](readme/testing/lighthouse_desktop.PNG)

When I first tested, my SEO score was quite low. I found that this was because I had forgotten the description, author and keywords information for the meta tag. To fix this, I added this information in to the meta tag and as a result, my score improved to 90%. The only issue currently still highlighted is the wording used for my links on the home page. They are flagged as not descriptive of the links, however I feel amending them to 'click here' as suggested, would change the feel of the site and be less descriptive so I have decided to keep them as they are.

### Mobile

![Lighthouse Mobile Score](readme/testing/lighthouse_mobile.PNG)

The only detractor on the mobile view is the same as on the desktop view- the wording for the links, which have not been amended as explained above.

## Browser Compatability

Google Chrome, Microsoft Edge, Mozilla Firefox and Safari all display content and images correctly and all links work and open in new window.
This was tested on a laptop, PC, iPad, Iphone SE, Galaxy S8 and a Motorola G9.

## Validators

### HTML

![HTML validation]()

No errors were found

### CSS

There were numerous errors caused by Bootstraps classes, but when pasting in my custom css, no errors or warnings were found were found.

### JavaScript

There is only 1 function in the script.js file, for closing messages after 3 seconds. I removed the alert variable as it wasn't necessary, and came up with a warning as the variable'bootstrap' wasn't defined. I retested the messages with this line removed and it still worked as expected.

### Python

![Pep8online Testing]()

[Pep8online.com](http://pep8online.com) was used to test all python files. All efforts were made to make all code pep8 compliant, with the exception of the settings.py file, which Django state in their docs is okay to ignore should it make the code ugglier or harder to read, which in these cases it does.

## User Stories

### As a **New Student** I can...

| Checked | ...**find a teacher online** so that **I can learn more about that person.**                                                                        |
| :-----: | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| &check; | With an SEO score of 100, I have made it as likely as possible to be found on search engine, and the home page is clear about what the site offers. |

| Checked | ...**see who I am taking lessons with** so that **I can feel comfortable meeting a new teacher.** |
| :-----: | :------------------------------------------------------------------------------------------------ |
| &check; | Video of myself playing drums on the home page, and a detailed 'about me' section                 |

| Checked | ... **see whether the teacher teaches children** so that **I know I am safe to leave my child during the lessons.** |
| :-----: | :------------------------------------------------------------------------------------------------------------------ |
| &check; | In the FAQs section this question has been covered direclty.                                                        |

| Checked | ...**find out if I am too old to start taking lessons** so that **I can avoid wasting my time** |
| :-----: | :---------------------------------------------------------------------------------------------- |
| &check; | Also covered in FAQs                                                                            |

| Checked | ...**book exact time slots** so that **I can plan the lessons around my life.** |
| :-----: | :------------------------------------------------------------------------------ |
| &check; | Bookings page with Calendly built in to book 60 minute slots.                   |

| Checked | ...**Get in touch before booking a lesson** so that **I can ask him any questions that aren't on the site** |
| :-----: | :---------------------------------------------------------------------------------------------------------- |
| &check; | Email address listed in the footer, and FAQs section                                                        |

| Checked | ...**get stuck in and play along at the same time as Tom** to that **I don't have to stop playing for him to demonstrate something.** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------------------ |
| &check; | Answered in FAQs, and imagery throughout the site.                                                                                    |

| Checked | ...**see reviews from real people** to that **I can find out if Tom is a good teacher for me.** |
| :-----: | :---------------------------------------------------------------------------------------------- |
| &check; | Reviews page                                                                                    |

## As a **Current Student** I can...

| Checked | ...**Login to my account** so that **I don't have to enter my details everytime I use the site**      |
| :-----: | :---------------------------------------------------------------------------------------------------- |
| &check; | If the user has cookies enabled, they can stay logged in to their profile when returning to the site. |

| Checked | ...**submit a review on Tom's site** so that **I can share my experience** |
| :-----: | :------------------------------------------------------------------------- |
| &check; | Reviews page                                                               |

| Checked | ...**browse the available jobs (brief description only)** so that **I can see if I wish to register with the site or not** |
| :-----: | :------------------------------------------------------------------------------------------------------------------------- |
| &check; | Can see the preview cards for available jobs                                                                               |
| &check; | Can see I need to sign up/log in to see more info                                                                          |

[Return to README.md](README.md)