---
Title: Yet another "outsider lands a coding job" success story
Date: 2022-08-20
Author: Jeff Nicholas
Status: draft
Dropcap: true
---

There is a seemingly infinite number of cases of non-tech people getting in to the tech industry, more than enough for other outsiders to feel good about their odds of making the same career change. I've seen it happen with a few musician friends/acquaintances, and read countless blogs and reddit posts about people describing how they got coding jobs without a "real" coding background. This is my entry into that storied tradition.

I landed my first fulltime coding job in the summer of 2022. I don't have an academic background in programming, and I never attended a boot camp or took a single programming class. Everything I learned came from online tutorials (primarily [Codecademy](https://www.codecademy.com/learn/learn-python-3){:target="_blank"} and [freeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/){:target="_blank"}) and personal projects, with plenty of Google and Stack Overflow sprinkled in. I actually had to stop myself from writing this article as soon as I got the job, because for every story about someone like me getting such a job there is another story about that same person feeling out of their depth in their new field. Was I going to end up in the same boat? Would I get exposed as some kind of fraud and get let go within two months?

By the grace of (the coding) god(s), I held on to that job for two and a half years. Next week I'll be starting a new fully remote job as a Backend Developer II with a 38% salary increase from my first full-time job. I owe some measure of success to [@powerbottomdad1](https://x.com/powerbottomdad1){:target="_blank"}, who wrote a [series of blog posts](https://lowlyswe.substack.com/p/my-experience-getting-a-tech-job){:target="_blank"} detailing his journey into tech as a non-techie which inspired me to jump headfirst into the job market. In the same spirit I will try to articulate how I landed that job and grew from there.

(somewhere before the next section write about why am I writing this, who it's meant for, yada yada)

## [My Background (or lack thereof)](#my-background){#my-background}

I went to school for music. I got my bachelor's degree in general music (with a focus on piano performance) and my master's degree in music composition. I taught a few adjunct courses after graduating and filled the rest of my time by teaching piano privately, neither being particularly lucrative. Academia never seemed to me an avenue worth going down, and piano lessons were a total crapshoot; students would leave for weeks or months during summer vacation and wouldn't always resume lessons when school started back up, they would frequently cancel last minute and leave me twiddling my thumbs, and worst of all they would sometimes fail to pay on time or at all. Needless to say, I reached a point where this lifestyle lost its luster and drove me to change careers.

The upside of teaching piano was the hours: most of my students were in grade school, so I wouldn't start teaching until around 4pm. This meant that I had all morning and early afternoon to do whatever I wanted, and at some point I decided to use that time to teach myself how to code (more on that later). I didn't have any relatives whose knowledge I could tap into (my dad is a social worker and my mom is an artist) and no money to pay for more schooling, so I embarked on this journey completely alone and in the dark.

Which is to say: if I can do it, literally anyone can.

## [🎵Take Me Out To The Code Game🎶](#take-me-out-to-the-code-game){#take-me-out-to-the-code-game}

It begins with fantasy baseball. The year was 2018. I wasn't really looking to make a career change; I just wanted to win my highly-competitive (i.e., $50 ante) fantasy baseball league. I had spent years at the bottom of the standings, even though I would follow certain internet personalities' rankings and strategies and thus thought I was well-informed, so I endeavored to reverse my fortunes by going about things my own way. Rather than use stats that were well known and widely used within the industry, I figured I'd be better off concocting a bespoke player evaluation system&mdash;at the very least, I'd be using a different system from everyone else.

With this as my starting position, I had to decide what programming language I was going to use to achieve my goals. Since I would be doing data science and analysis (probably too strong of words to describe what I actually did), the internet told me that Python would be ideal. It's hard to say with the benefit of hindsight if this was a good thing or not; I did end up "making it" in terms of getting a job and whatnot, but maybe my path would've been shorter and easier had I started with a language that more employers use (e.g. Java, C#, JavaScript). Regardless, Python is what I dove into and tried to master, using the Codecademy course linked above.

My goal was to automate the process of adding and removing players to and from my lineup using the algorithms that I created for evaluating players. Basically what I did was scrape my lineup and the available free agents from our league platform's website every morning and run it through various formulas to determine if there were any hitters on the market that had better match-ups that day than players on my team. Any free agents with better daily match-ups were automatically added to my team after the player they replaced was dropped.

I didn't start using this script until late in the season, by which time it was far too late to come back from being near last place. However, I did make a push and finish several spots higher when all was said and done, and overall I felt not only a sense of accomplishment because of the script's marginal success but that coding was something I could do fulltime because of how satisfying it was creating a piece of software and watching it work its magic.

Luckily for me, an opening for a data scientist at a well known baseball website became available not long after I had done all this work. Following the conclusion of the 2019 MLB season, I saw this position open up via a twitter post and scrambled to put together an application. I wrote a short essay detailing my methodologies and crunched some numbers to show how "well" my script worked and sent it along with the full Python script. Before long, I had an interview and a job offer. Granted, this was a part-time position (and I'm still there, by the way, now as Senior Database Engineer), but my foot was in the door.

## [Getting Up to Speed](#getting-up-to-speed){#getting-up-to-speed}

It's tough to say if getting this part-time role is what enabled all my future successes, but it certainly *feels* like that's the case. Without this job my résumé would've been nothing more than personal projects&mdash;which maybe in some instances is enough, but since I didn't have any apropos credentials probably wouldn't have been enough for someone like me.

This job also taught me a lot of skills and introduced me to technologies relevant to the industry writ large, like version control and what an API is. When I started I didn't even know what a web developer really did or that backend and frontend developers were a thing, and I certainly didn't expect that I would eventually be transitioning into backend web development. It would be several more years before I felt comfortable trying to completely change the course of my life by moving away from music and into software development.

In the meantime, I got as good at data science as I could. I learned the pandas and NumPy libraries; scikit-learn and SciPy; matplotlib and seaborn; I learned about generalized additive models and Jupyter notebooks (totally unrelated things, I know). All of this was stuff I learned on my own, too; I completed several data science courses offered by IBM and Kaggle (and got cute little certificates to boot), and I also bought a [Python textbook](https://www.amazon.com/Python-Programming-Introduction-Computer-Science/dp/1887902996){:target="_blank"}, reading it cover-to-cover and doing every coding problem at the end of each chapter. I probably wouldn't have done any of this had I not gotten this job, so at the very least it instilled in me the drive to learn more and do a better job (otherwise I'd get fired, was the thought in my head).

I did all of this while alongside my work tasks for about two years before my uncle came to me with a project: create a website where he could use his home-brewed formulas for betting on baseball games. This is where I discovered what a web developer's job looks like, specifically a fullstack developer. I built a backend server with Flask and taught myself HTML/CSS/JavaScript and how HTML templating works via jinja, after a few weeks of grinding I had a fully functioning site that my uncle was using to bet on live games. More than that, I had a new hobby horse: web development.

I took this experience and helped my artist mom build an e-commerce site where she could sell her paintings. She had been selling her artwork on Etsy for years but had grown disillusioned with their business model, so I took it upon myself to create a site for her from scratch (more as a learning experience for myself than something she could pivot to and abandon Etsy). This was another few weeks of grinding and learning the basics of CRUD applications (again using Flask and jinja), the end result being another fully functioning site (I say "fully functioning" slightly tongue-in-cheek because it's obviously not some major accomplishment, but for someone with background it was *something*).

Fullstack development became fun for me after these projects, so I took a closer look at the frontend aspect and discovered React. I wasn't sure if I was going to try getting a job as a fullstack developer, but I figured it couldn't hurt my chances of getting a job by learning this massively popular JavaScript framework. Around the same time Wordle went viral, and it gave me the idea to make a game where players have to guess planes from pictures (extremely nerdy, but my dad is an aviation buff so I thought it'd be something fun for him and I to do). I found a free API for plane photos and built another Flask backend, but this time instead of serving jinja templates I created an API that my React frontend could hit. This was probably overkill, but it was a good way for me to learn that went well beyond basic tutorials. In the end I created [spottheplane.net](https://www.spottheplane.net/){:target="_blank"}, and it was at this point that I felt it was time.

## [The Big Break](#the-big-break){#the-big-break}

I was teaching piano while doing all of this; I even got a gig playing piano at a tiny church in rural Ohio, because I was still trying to make ends meet. By the summer of 2022 I finally decided that I had done enough to start looking for fulltime software jobs in earnest. I'm not usually one to take charity or ask people for favors, so rather than try to leverage people from the baseball site for work I decided to cast my résumé to the wind (i.e., apply to jobs through Indeed.com).

I remember not being very hopeful, especially when the rejections started to roll in. I think I applied to something like 60 jobs, mostly within the area of northwest Ohio I was living in, and for a while I either didn't get a response or if I did get a response it was a rejection. A recruiter from one place reached out to me and wanted to set something up, but it seemed shady to me or at the very least not appealing.

## [Climbing the Ladder](#climbing-the-ladder){#climbing-the-ladder}

(write about getting porch and job hunting generally)

## [Coda](#coda){#coda}

(summary)
