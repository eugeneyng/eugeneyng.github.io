AUTHOR = "Eugene Ng"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = False
PATH = "content"
RELATIVE_URLS = True # Uncomment if you want document-relative URLs when developing
SITENAME = "Eugene Ng"
SITEURL = ""
TIMEZONE = "America/New_York"

# Theme
THEME = "./pelican-resume"

# Profile information
NAME = "Eugene Ng"
TAGLINE = "Engineer"
PIC = "profile.png" # Make sure you put a profile.png in your ./content folder

# Sidebar links
EMAIL = "eyn2@cornell.edu"
PHONE = "860 726 6143"
WEBSITE = "eugene.ng"
# PORTFOLIO = "portfolio.eugene.ng"
LINKEDIN = "eugeneyng"
GITHUB = "eugeneyng"
PDF = "https://raw.githubusercontent.com/eugeneyng/eugeneyng.github.io/pelican/content/docs/resume.pdf"

CAREER_SUMMARY = "I am a technical operations director with 10 years of experience managing fast-paced military and commercial contracts at Pratt & Whitney, a division of Raytheon Technologies. My company Presque Labs LLC has won or finalized in multiple design challenges (HeroX, YCombinator). In my free time I love to stay active and play volleyball, tennis, and ski."

EDUCATION = [
	{
		"degree": "M. Eng, Electrical Engineering",
		"institution": "University of Connecticut",
		"time": "2018 - 2020"
	},
	{
		"degree": "M. Eng, Mechanical Engineering",
		"institution": "Cornell University",
		"time": "2016 - 2017"
	},
  {
    "degree": "B.S., Mechanical Engineering",
    "institution": "Cornell University",
    "time": "2012 - 2016"
  }
]

EXPERIENCES = [
  {
    "job_title": "Associate Director, Manufacturing Engineering & Operations",
    "time": "May 2024 - Present",
    "company": "Pratt & Whitney | Raytheon Technologies Corp",
    "details": [
      {
        "description": "Developed and maintained capital expenditure models to support business forecasting and budgeting processes, including cash management, capacity needs, and strategic initiatives"
      },
      {
        "description": "Responsible for long range (capital) planning across all P&W Operations, Engineering, and Aftermarket (MRO) module centers, totaling >$500M per year in machine tool, tooling, and facilities spend"
      },
      {
        "description": "Managed strategic supplier relationships and was primary point of escalation for contract enforcement and disputes. Provided data-driven supplier scorecards and health metrics for machine tools to support negotiations and Master Terms Agreements (MTAs)"
      },
      {
        "description": "Led team of ten project managers responsible for executing more than $200M of machine tool procurement yearly"
      }
    ],
  },
  {
    "job_title": "Various Positions, Manufacturing Engineering & Operations",
    "time": "Feb 2017 - May 2024",
    "company": "Pratt & Whitney | Raytheon Technologies Corp",
    "details": [
      {
        "description": "Established and maintained general equipment standards across P&W, with cross-functional feedback from EH&S, MTS, and Manufacturing Engineering teams"
      },
      {
        "description": "Modernized and established new procurement workflows in AgilePoint and Appian, and helped reduce process times by up to 20%, or more than 60 days"
      },
      {
        "description": "Led team of five developers to design and program the largest (to-date) AgilePoint and Appian application at RTX for capital execution"
      },
      {
        "description": "Oversaw procurement of hundreds of capital equipment projects totaling more than $25M per year",
        "inner_details": [
          "Wrote technical specifications identifying critical processes and guiding design concepts for external vendors",
          "Negotiated commercial (pricing, payment structure) and legal terms and conditions to reduce cost and risk",
          "Validated and led acceptance tests for all projects, including material handling automation equipment, machining and inspection systems, and CNC and welding equipment, etc.",
          "Provided EAR and ITAR classifications for export of sensitive technical data.",
        ]
      }
    ],
  },
  {
    "job_title": "Co-Founder",
    "time": "Jul 2015 - Present",
    "company": "Presque Labs LLC",
    "details": [
      {
        "description": "HeroX NextGen Cart Design Challenge winner for airport material transport (AMTC) concept to track and transport secured goods within an airport (2018)",
        "inner_details": [
          "Designed electrical circuit in KiCad and prototyped and fabricated PCB through OSH Park",
          "Developed user interface and linked IoT sensors to SQL database using Python",
        ]
      },
      {
        "description": "Full stack programming with Flask, Django, and MongoDB for Waddle, an events app (2022)",
      },
      {
        "description": "Generated concepts for Revocube (a 3D puzzle game) and programmed game in Unity with C# (2017)",
      },
      {
        "description": "Built and programmed Context, a text message analytics app, in Android Studio with Java (2016)",
      },
      {
        "description": "Maintained and provided site reliability engineering for company website and internal applications, including Docker, Jupyter, Nginx, Nextcloud, and Wordpress",
      }
    ]
	}
]

INTERESTS = [
  {
    "item": "Piano",
    "link": "https://www.youtube.com/channel/UCq9CWmdBPJ167Vo3cEH_Erw"
  },
  {
    "item": "Skiing",
    "link": "https://www.youtube.com/channel/UCq9CWmdBPJ167Vo3cEH_Erw"
  },
  {
    "item": "Tennis",
    "link": "https://www.youtube.com/channel/UCq9CWmdBPJ167Vo3cEH_Erw"
  },
  {
    "item": "Volleyball",
    "link": "https://www.youtube.com/channel/UCq9CWmdBPJ167Vo3cEH_Erw"
  }
]

LANGUAGES = [
	{
		"name": "English",
		"description": "Native"
	}
]

PROJECT_INTRO = ""

PROJECTS = [
	{
		"title": "Nonlinear Optimal Control of the COVID-19 Pandemic in Connecticut (2020)",
    "details": [
      {
        "description": "Created a modified SEIR model of COVID-19 spread in Connecticut, and formulated a discrete, nonlinear, predictive, closed-loop feedback controller to minimize the number of infected."
      },
      {
        "description": "Simulated mathematical model in Python using the GEKKO optimization suite"
      }
    ],
    "link": "https://raw.githubusercontent.com/eugeneyng/eugeneyng.github.io/pelican/content/docs/engr5315.pdf"
	},
	{
		"title": "HeroX NextGen Cart Design Challenge | Presque Labs LLC (2018)",
		"details": [
      {
        "description": "Challenge winner for airport material transport (AMTC) concept to track and transport secured goods within an airport."
      },
      {
        "description": "Designed electrical circuit in KiCad and prototyped and fabricated PCB through OSH Park."
      },
      {
        "description": "Developed user interface and linked IoT sensors to SQL database using Python."
      },
    ],
    "link": "https://www.herox.com/nextgen-cart-design-challenge"
	},
	{
		"title": "Arachnabot, Spider-Inspired Robot | Collective Embodied Intelligence Lab (2016)",
    "details": [
      {
        "description": "Analyzed, modeled, and simulated a to-scale jumping robot with spider-inspired joints in MATLAB, using a differential algebraic equation (DAE) method."
      },
      {
        "description": "Directed micro-fabrication using FDM and SLA 3D printing methods"
      }
    ],
    "link": "https://raw.githubusercontent.com/eugeneyng/eugeneyng.github.io/pelican/content/docs/arachnabot.pdf"
	},
  {
		"title": "Cornell Concrete Canoe (2016)",
    "details": [
      {
        "description": "3rd place finish at 2016 ASCE Concrete Canoe Competition."
      },
      {
        "description": "Coordinated and oversaw 6 subteams (aesthetics, analysis, business, mold, mix, and paddling) and 34 persons for the 2016 ASCE Concrete Canoe Competition."
      },
      {
        "description": "Introduced novel moisture sensors and concrete curing control."
      },
      {
        "description": "Eliminated shrinkage cracking while increasing tensile and compressive strength by 62% and 35%"
      }
    ],
    "link": "https://raw.githubusercontent.com/eugeneyng/eugeneyng.github.io/pelican/content/docs/thrakos.pdf"
	},
]

SKILLS = [
	{
    "title": "ANSYS",
    "level": "75"
  },
  {
    "title": "HTML/CSS/JavaScript",
    "level": "95"
  },
  {
    "title": "KiCad",
    "level": "75"
  },
  {
    "title": "LaTeX",
    "level": "95"
  },
  {
    "title": "MATLAB",
    "level": "95"
  },
  {
    "title": "Microsoft Access",
    "level": "95"
  },
  {
    "title": "Python",
    "level": "95"
  },
  {
    "title": "React/Vue",
    "level": "85"
  },
  {
    "title": "Solidworks",
    "level": "75"
  },
  {
    "title": "Visual Basic for Applications (VBA)",
    "level": "95"
  },
  {
    "title": "Structured Query Language (SQL)",
    "level": "90"
  },
  {
    "title": "Wordpress",
    "level": "75"
  }
]
