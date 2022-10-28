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

- Issue - SEO score was quite low.
- Cause - I had forgotten the description, author and keywords information for the meta tag and SEO's weren't picking up 'read more' on my article links.
- Solution - I added this information in to the meta tag and amended the links to read 'learn more'.

## Wave Aim Accessibility Checker

## Lighthouse

### Desktop

![Lighthouse Desktop Score](readme-content/testing/testing-lighthouse-desktop.png)

I spent some time altering how the home page video renders, as this was causing a lot of extra load time. The background images on the home page was also taking a while due to its size. I added some media queries to help with this by loading a size similar to the viewport, which drastically reduces the file size

### Mobile

![Lighthouse Mobile Score](readme-content/testing/testing-lighthouse-mobile.png)

The scores mainly fluctuated between 80-95, mainly around 87/88, however the recurring issue was the unused CSS and JS caused by using the Bootstrap CDN, meaining the initial render was slower than it could have been. I'll consider looking at other alternatives like Tailwind for future projects should I use another framework, as it optimizes the file size based on used CSS.

## Validators

### HTML

![HTML validation](readme-content/testing/testing-html.png)

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