# -*- coding: utf-8 -*-
"""
Static site generator for Sree Suraksha Multispeciality Hospital.
Run: python build/generate.py
Regenerates every HTML page from the data below into the project root,
using folder/index.html so URLs match the original site (e.g. /contact-us).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = {
    "name": "Suraksha Multispeciality Hospital",
    "full_name": "Sree Suraksha Multispeciality Hospital",
    "unit_of": "A Unit of Viyan Sri Health Care Pvt. Ltd.",
    "phones": ["+91 96664 69911", "+91 7288 080 222", "+91 7288 080 333"],
    "phone_href": "+919666469911",
    "email": "info@sushrutamedicalservices.com",
    "address": "6-1540/DNP/G1. Beside Reliance Trends, Near Allur Seetharamaraju Statue, Pragathi Nagar, Hyderabad-500090.",
    "social": {
        "facebook": "https://www.facebook.com/profile.php?id=61561176598161",
        "twitter": "https://x.com/sreesuraksha",
        "instagram": "https://www.instagram.com/sreesurakshahospital1/?hl=en",
        "linkedin": "https://www.linkedin.com/company/104222176/",
        "youtube": "https://www.youtube.com/@SreeSurakshahospital",
    },
    "map_embed": "https://www.google.com/maps?q=Pragathi+Nagar,+Kukatpally,+Hyderabad,+Telangana,+India&output=embed",
}

NAV_LINKS = [
    ("Home", "/"),
    ("Our Services", "/our-services/"),
    ("Blog", "/blog/"),
    ("Contact Us", "/contact-us/"),
]

FOOTER_QUICK_LINKS = [
    ("Home", "/"),
    ("Our Services", "/our-services/"),
    ("Blog", "/blog/"),
    ("Contact Us", "/contact-us/"),
]

FOOTER_SERVICE_LINKS = [
    ("General Medicine", "/general-medicine/"),
    ("Diabetology", "/diabetology/"),
    ("Paediatrics & Neonatology", "/paediatrics-and-neonatology/"),
    ("Orthopaedics", "/orthopaedics/"),
    ("Trauma & Critical Care", "/trauma-and-critical-care/"),
    ("Joint Replacement", "/joint-replacement/"),
]

# Home page — featured services (6 cards)
HOME_SERVICES = [
    {"slug": "general-medicine", "title": "General Medicine", "img": "services/services-1.jpg",
     "desc": "We at Sree Suraksha Multi-specialty Hospital have the best General Medicine department that is dedicated to the delivery of quality healthcare services with professionalism and warmth."},
    {"slug": "diabetology", "title": "Diabetology", "img": "services/services-2.jpg",
     "desc": "Sri Suraksha Multi-specialty Hospital has a dedicated Diabetology department focusing on proper treatment and management of diabetes, provided by competent endocrinologists and diabetes care specialists."},
    {"slug": "paediatrics-and-neonatology", "title": "Paediatrics & Neonatology", "img": "services/paediatrics.jpg",
     "desc": "The Neonatology department is committed to delivering quality care to newborns and premature babies with a focus on the child's well-being."},
    {"slug": "orthopaedics", "title": "Orthopaedics", "img": "services/services-3.jpg",
     "desc": "Orthopedics at Sree Suraksha is among the largest orthopedic treatment services in Hyderabad for your bone and joint treatment."},
    {"slug": "trauma-and-critical-care", "title": "Trauma & Critical Care", "img": "services/services-4.jpg",
     "desc": "Our Trauma & Critical Care Unit is committed to providing the best emergency services with modern medical facilities and professional staff."},
    {"slug": "joint-replacement", "title": "Joint Replacement", "img": "services/services-5.jpg",
     "desc": "Our Joint Replacement department aims to give new-age solutions to patients suffering from joint pains and other movement limitations."},
]

# Full A-Z department list (used on /our-services/ and footer sidebars)
DEPARTMENTS = [
    {
        "slug": "general-medicine", "nav_title": "General Medicine", "title": "General Medicine",
        "meta_title": "Best General Physician in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/services-1.jpg",
        "summary": "We at Sree Suraksha Multi-specialty Hospital have the best General Medicine department that is dedicated to the delivery of quality healthcare services with professionalism and warmth.",
        "paragraphs": [
            "We at Sree Suraksha Multi-specialty Hospital have the best General Medicine department that is dedicated to the delivery of quality healthcare services with professionalism and warmth. With the help of our team of experienced physicians and backed up by modern diagnostic and treatment equipment, we provide an individual approach to each patient and treat different diseases.",
            "Preventive health, chronic diseases like diabetes and hypertension, infections, and other complicated cases are some of the services offered. We focus on patient education, which enables people to make the right choices regarding their health.",
            "For those who need general health check up, specific appointments with a doctor, or immediate care, our staff is always ready to assist you. Sri Suraksha is our organization and your health is our main concern. Come to us for the best healthcare services.",
        ],
    },
    {
        "slug": "diabetology", "nav_title": "Diabetology", "title": "Diabetology",
        "meta_title": "Best Diabetes Care Clinic in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/services-2.jpg",
        "summary": "Sri Suraksha Multi-specialty Hospital has a dedicated Diabetology department focusing on proper treatment and management of diabetes.",
        "paragraphs": [
            "Sri Suraksha Multi-specialty Hospital has a dedicated Diabetology department focusing on proper treatment and management of diabetes. The services are provided by a team of competent endocrinologists and diabetes care specialists who work closely with each patient to develop a treatment plan.",
            "Our services comprise diabetes care, routine health check-ups and counseling, and complex treatment procedures for diabetic complications. We focus on patient engagement, enabling a person to understand how to deal with the situation and enhance the quality of life.",
        ],
    },
    {
        "slug": "paediatrics-and-neonatology", "nav_title": "Paediatrics & Neonatology", "title": "Paediatrics & Neonatology",
        "meta_title": "Best Pediatric Multispeciality Hospital in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/paediatrics.jpg",
        "summary": "The Neonatology department is committed to delivering quality care to newborns and premature babies.",
        "paragraphs": [
            "At Sri Suraksha Multi-specialty Hospital, the Neonatology department is committed to delivering quality care to newborns and premature babies. Our team of neonatologists and pediatric specialists provides high-quality medical care with a focus on the child’s well-being.",
            "We appreciate the unique requirements of newborns and aim to provide them with the best family-oriented care. Our services include neonatal intensive care, developmental, nutritional, and medical neonatal care.",
            "Our team has access to the most modern equipment and guidelines that allow us to provide the best quality of neonatal care to young patients. Whether your newborn needs critical care or a simple examination, Sri Suraksha is the best place to go for professional care and understanding.",
        ],
    },
    {
        "slug": "orthopaedics", "nav_title": "Orthopaedics", "title": "Orthopaedics",
        "meta_title": "Best Orthopedic Treatment in Pragathi Nagar, Hyderabad | Sree Suraksha Hospitals",
        "banner": "services/services-3.jpg",
        "summary": "Orthopedics at Sree Suraksha is among the largest orthopedic treatment services in Hyderabad for your bone and joint treatment.",
        "paragraphs": [
            "Orthopedics in SREE Suraksha Multi-Speciality Hospital is among the largest orthopedic treatments service hospitals in Hyderabad for your bone and joint treatment. Some of our specialties include a number of creative treatment plans which are in line with the patients’ healthcare requirements and are designed to give the highest services and coverage possible.",
        ],
        "conditions": [
            ("Arthritis", "Joint inflammation which results in pain and stiffness in affected joints and can be treated by medication, physical therapy and in severe cases surgery."),
            ("Bursitis", "This is inflammation of the fluid filled sacs known as bursae, which are located near joints, and is usually treated through rest, ice, medications or injections."),
            ("Chronic Muscle Joint Pains", "Chronic pain in muscles or joints that need proper assessment and management through tailored interventions."),
            ("Multiple Fractures", "In the treatment of multiple bone breaks, surgical management, immobilization, and rehabilitation to enhance the healing process."),
            ("Replacement (TKR / THR)", "Arthroplasty surgery for patients suffering from osteoarthritis, rheumatoid arthritis, or traumatic arthritis and requiring Total Knee Replacement (TKR) or Total Hip Replacement (THR)."),
            ("Non Cancerous Benign Tumors", "Surgical or medical intervention to address benign growths that target bones or soft tissues."),
            ("Cancerous Tumors", "Cancer which affects the bones or soft tissues and its diagnosis as well as surgical intervention."),
            ("Arthroscopy (Shoulder / Knee)", "Arthroscopy, which involves inserting a small camera to identify and address joint issues such as injuries and swelling."),
            ("Trauma & Fracture", "Trauma management involving operations and fracture fixation."),
            ("Spine Surgery", "Invasive procedures aimed at the spine, such as microdiscectomy, laminectomy, or correction of scoliosis."),
            ("Musculoskeletal Disorders", "Comprehensive care for various ailments that have an impact on muscles, bones, and joints, helping patients regain their mobility and improve their quality of life."),
            ("Sports Injuries", "It involves assessment of sports related injuries and treatment to ensure early return to sport and physical activity."),
            ("Physiotherapy", "This is the use of exercise and physical treatment procedures to enable the patient regain his or her mobility after an injury or surgery."),
        ],
    },
    {
        "slug": "trauma-and-critical-care", "nav_title": "Trauma & Critical Care", "title": "Trauma & Critical Care",
        "meta_title": "Trauma and Critical Care Hospital in Kukatpally, Hyderabad | Sree Suraksha Hospitals",
        "banner": "services/services-4.jpg",
        "summary": "Our Trauma & Critical Care Unit is committed to providing the best emergency services with modern medical facilities and professional staff.",
        "paragraphs_headed": [
            (None, "Our Trauma & Critical Care Unit at Sree Suraksha Multispeciality Hospital is committed to providing the best of emergency services with the help of modern medical facilities and professional staff. We are prepared to deal with almost any type of injury and severe conditions, and we provide round-the-clock services for quick and efficient treatment."),
            ("Comprehensive Trauma Services", "Our trauma center is fully manned by professional trauma surgeons, orthopedic surgeons, and neurosurgeons who work as a team. We emphasize the initial evaluation and stabilization of patients in order to provide them with the required treatment as soon as possible."),
            ("Advanced Critical Care", "Our Critical Care Unit (CCU) is equipped with modern equipment of monitoring and life support that offer close, intensive care to patients with critical diseases. The experienced staff of intensivists, critical care nurses, and respiratory therapists in our unit develop individual treatment plans to optimize results."),
            ("Patient-Centered Approach", "Our main focus is the patient, and we ensure that they are comforted and receive all the help they need during the healing process. Trust Sree Suraksha Multispeciality Hospital for the best trauma and critical care service when it is required the most."),
        ],
    },
    {
        "slug": "joint-replacement", "nav_title": "Joint Replacement", "title": "Joint Replacement",
        "meta_title": "Robotic Knee Replacement Surgery in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/services-5.jpg",
        "summary": "Our Joint Replacement department aims to give new-age solutions to patients suffering from joint pains and other movement limitations.",
        "paragraphs": [
            "Our Joint Replacement department in Sri Suraksha Multi-specialty Hospital aims to give new age solutions to patients who are suffering from joint pains and other movement limitations. Our staff comprises highly skilled and qualified orthopedic surgeons in performing complex joint replacement surgeries such as hip, knee, and shoulder replacements.",
            "With the help of the most advanced methods and modern equipment, we strive to help our patients regain the ability to move and enhance their quality of life. The treatments that we offer include consultation before the surgery, tailored treatment, surgery that is less invasive, and physiotherapy after the surgery.",
            "The focus is on the patient’s education and encouragement, which means that you will be explained every stage and will not have any doubts regarding your choice. It is our aim to get you back to the activities you love without discomfort as soon as it is possible and safe to do so.",
        ],
    },
    {
        "slug": "general-and-laparoscopic-surgery", "nav_title": "General & Laparoscopic Surgery", "title": "General & Laparoscopic Surgery",
        "meta_title": "Advanced Laparoscopic Surgery in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/services-6.jpg",
        "summary": "The General & Laparoscopic Surgery department delivers quality surgical services with modern instruments and customer-oriented solutions.",
        "paragraphs_headed": [
            (None, "The General & Laparoscopic Surgery department of Sree Suraksha Multispeciality Hospital delivers quality surgical services with modern instruments and customer-oriented solutions. All of our surgeons are fully qualified and skilled in a range of surgeries with a focus on the laparoscopic method to reduce the patient’s pain and time spent in the hospital."),
            ("Comprehensive Surgical Services", "We perform operations for diseases such as gallstones, hernias, and appendicitis with open and minimally invasive techniques to achieve the best results."),
            ("Patient-Centered Care", "It is our honor to serve the patient from the preoperative consultation to the postoperative follow-up to guarantee the comprehensive care of every patient."),
        ],
    },
    {
        "slug": "surgical-gastroenterology", "nav_title": "Surgical Gastroenterology", "title": "Surgical Gastroenterology",
        "meta_title": "Best Gastroenterology Hospital near Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/gastroenterology.jpg",
        "summary": "The Surgical Gastroenterology department deals with the diagnosis and surgical management of gastrointestinal diseases.",
        "paragraphs_headed": [
            (None, "The Surgical Gastroenterology department at Sree Suraksha Multispeciality Hospital deals with the diagnosis and surgical management of gastrointestinal diseases. Our staff specializes in the treatment of various disorders such as gastrointestinal malignancies, Crohn’s disease, ulcerative colitis, and complicated liver and pancreatic disorders."),
            ("Advanced Surgical Care", "We provide latest and advanced surgical procedures such as laparoscopic and other robotic surgeries; patients have less pain and faster recovery time."),
            ("Patient-Focused Approach", "We have a committed staff that offers medical support from the time of diagnosis, to the time of surgery and even after surgery."),
        ],
    },
    {
        "slug": "medical-gastroenterology", "nav_title": "Medical Gastroenterology", "title": "Medical Gastroenterology",
        "meta_title": "Medical Gastroenterology Hospital in Pragathi Nagar, Kukatpally | Sree Suraksha Hospitals",
        "banner": "services/medical-gastroenterology.jpg",
        "summary": "A Medical Gastroenterology department committed to offering quality services to patients with various gastrointestinal disorders.",
        "paragraphs": [
            "Sri Suraksha Multi-specialty Hospital has a Medical Gastroenterology department that is committed to offering quality services to patients with various gastrointestinal disorders. Our staff of highly qualified gastroenterologists works diligently to diagnose and treat a wide range of gastrointestinal disorders.",
            "Some of our specialized services are endoscopy and colonoscopy, IBD/IBS, liver diseases, and nutritional support. We embrace technology and research findings in diagnosis and treatment of patients to enhance efficiency.",
            "The main concept that is followed here is patient centered care. We involve the patient in the development of treatment plans that will meet the required goals and maintain digestive health. Whether it is a simple stomach upset or a chronic gastrointestinal disease, Sri Suraksha is the place to go for professional services.",
        ],
    },
    {
        "slug": "neurology", "nav_title": "Neurology", "title": "Neurology",
        "meta_title": "Best Neurologist Specialist Hospital in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/neurology.jpg",
        "summary": "Our Neurology department is dedicated to providing exceptional care for patients with neurological disorders.",
        "paragraphs": [
            "At Sri Suraksha Multi-specialty Hospital, our Neurology department is dedicated to providing exceptional care for patients with neurological disorders. Our team of highly skilled neurologists and specialized medical staff is committed to diagnosing and treating a wide range of conditions affecting the brain, spinal cord, and nervous system.",
            "Our services include sophisticated diagnostic tests, long-term care of conditions like epilepsy, multiple sclerosis, and Parkinson’s disease, and acute neurological conditions like stroke. We have modern equipment and the latest technology to help in diagnosis and treatment of our patients.",
            "Our patients’ health is always our main concern. In this respect, we stress comprehensive care strategies with individualized treatment recommendations for each client. Right from the time of consultation, the treatment, and even the rehabilitation process, our caring staff is with you.",
        ],
    },
    {
        "slug": "neuro-surgery", "nav_title": "Neuro Surgery", "title": "Neuro Surgery",
        "meta_title": "Best Neuro Surgeon in Pragathi Nagar, Hyderabad | Sree Suraksha Hospitals",
        "banner": "services/neurosurgery.jpg",
        "summary": "Neurosurgery is one of the top specializations of Sree Suraksha Multispeciality Hospital.",
        "paragraphs_headed": [
            (None, "Neurosurgery is one of the top specializations of the Sree Suraksha Multispeciality Hospital that provides the best treatments to the patients with neurological disorders. Our highly qualified neurosurgeons practice in the diagnosis and management of brain, spine, and peripheral nerve conditions."),
            ("Advanced Neurosurgical Care", "We embrace modern technology and perform surgeries with the least invasiveness for diseases like brain tumors, spinal injuries, aneurysms, and other spinal diseases that result from degeneration."),
            ("Comprehensive Patient Care", "Our staff is committed to offering patients professional attention, starting with the consultation and followed by surgery and rehabilitation to achieve the best results."),
        ],
    },
    {
        "slug": "oncology", "nav_title": "Oncology", "title": "Oncology",
        "meta_title": "Best Surgical Oncology Specialist in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/oncology.jpg",
        "summary": "The Oncology department offers cancer treatment and support with the latest techniques.",
        "paragraphs_headed": [
            (None, "The Oncology department of Sree Suraksha Multispeciality Hospital aims at offering cancer treatment and support in the best possible ways with the help of the latest techniques. Our staff comprises professional oncologists who focus on cancer detection and treatment such as breast, lung, colorectal, and blood cancer."),
            ("Advanced Cancer Treatment", "Some of the treatments include chemotherapy, radiation therapy, immunotherapy, and targeted therapy using modern technology to enhance the efficiency of the treatment."),
            ("Patient-Centered Care", "Emphasis is on the comprehensive care of the patient, involving the emotional and psychological as well as the medical, from the time of diagnosis to the time of recovery."),
        ],
    },
    {
        "slug": "ent", "nav_title": "ENT", "title": "ENT",
        "meta_title": "Best ENT Hospital near Pragathi Nagar, Hyderabad | Sree Suraksha Hospitals",
        "banner": "services/ent.jpg",
        "summary": "The ENT department is dedicated to providing quality care to patients with various ENT related disorders.",
        "paragraphs": [
            "The ENT department of Sri Suraksha Multi-specialty Hospital is dedicated to providing quality care to patients with various ENT related disorders. Our highly experienced ENT doctors are committed to the diagnosis, management, and treatment of patients with diseases of the ear, nose, throat, head, and neck.",
            "Our services include diagnostic tests, medical and surgical management of sinusitis, hearing disorders, voice disorders and sleep apnea. We have modern equipment and cutting edge treatment plans so that you get the best of services.",
            "Patient-centered care is the foundation of our practice. We create unique interventions based on the patient’s needs, which makes our solutions efficient and long-lasting. Whether you are coming in for a simple health check or for a surgery, our caring team is with you all through the process.",
        ],
    },
    {
        "slug": "dermatology", "nav_title": "Dermatology", "title": "Dermatology",
        "meta_title": "Best Skin Specialist Hospital in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/dermatology.jpg",
        "summary": "Comprehensive treatment for any skin, hair, and nail disorder.",
        "paragraphs_headed": [
            (None, "Our Dermatology department at Sree Suraksha Multispeciality Hospital provides comprehensive treatment for any skin, hair, and nail disorder. Our team of dermatologists is composed of highly skilled professionals who are capable of addressing all sorts of skin disorders such as acne, eczema, psoriasis, and skin infections."),
            ("Advanced Skin Care", "We provide the latest and advanced treatment procedures so that patients have less discomfort and faster recovery time."),
            ("Patient-Focused Approach", "We have a committed staff that offers medical support from the time of diagnosis, through treatment and follow-up care."),
        ],
    },
    {
        "slug": "pulmonology", "nav_title": "Pulmonology", "title": "Pulmonology",
        "meta_title": "Pulmonology Specialist Hospital in Kukatpally, Hyderabad | Sree Suraksha Hospitals",
        "banner": "services/pulmonology.jpg",
        "summary": "The Pulmonology department deals with respiratory diseases and related ailments.",
        "paragraphs_headed": [
            (None, "The Pulmonology department of Sree Suraksha Multispeciality Hospital deals with respiratory diseases and related ailments. Our highly trained and committed staff of pulmonologists offers treatment and diagnosis of conditions like asthma, COPD, pneumonia, and sleep apnea."),
            ("Advanced Respiratory Care", "We employ the latest diagnostic techniques and therapies, such as PFTs, bronchoscopy, and imaging, so that patients receive the right diagnosis and treatment."),
            ("Patient-Centered Approach", "At Sree Suraksha Multispeciality Hospital we value the physical, emotional, and social needs of the patient and provide care that involves the development of a comprehensive management plan for respiratory disorders with emphasis on rehabilitation."),
        ],
    },
    {
        "slug": "physiotherapy", "nav_title": "Physiotherapy", "title": "Physiotherapy",
        "meta_title": "Best Physiotherapy Specialist in Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/physiotherapy.jpg",
        "summary": "Physiotherapy aims at improving the patient's movement, activity level and overall well-being.",
        "paragraphs_headed": [
            (None, "Physiotherapy at Sree Suraksha Multispeciality Hospital aims at improving the patient’s movement, activity level and overall well-being of the patient. We have experienced physiotherapists who offer specialized physiotherapy services for various ailments such as musculoskeletal injuries, neurological conditions as well as post-surgical rehabilitation."),
            ("Comprehensive Rehabilitation Services", "We provide state of the art methods of treatment such as manual therapy, exercise therapy, electrotherapy and hydrotherapy among others depending on the patients."),
            ("Holistic Patient Care", "At Sree Suraksha Multispeciality Hospital, we believe in the multidimensional approach to physiotherapy, the goal of which is to enhance the quality of life and restore the patient’s ability to perform daily tasks with safe and effective treatments."),
        ],
    },
    {
        "slug": "radiology-and-intervention-radiology", "nav_title": "Radiology & Intervention Radiology", "title": "Radiology & Intervention Radiology",
        "meta_title": "Best Interventional Radiology Hospital in Hyderabad | Sree Suraksha Hospitals",
        "banner": "services/radiology.jpg",
        "summary": "Committed to delivering the best in imaging and invasive procedures.",
        "paragraphs": [
            "Radiology & Interventional Radiology at Sri Suraksha Multi-specialty Hospital is committed to delivering the best in imaging and invasive procedures. The radiology team consists of professional radiologists and interventional specialists who apply modern techniques to diagnose and treat various diseases.",
            "Diagnostic imaging services include X-rays, MRI, CT scans, and ultrasound while interventional procedures include angiography, biopsy, and image guided therapy among others. We value accuracy and the safety of our patients in all the procedures that we undertake to deliver quality services.",
            "The focus on the patient is our main principle. We give individual care and assistance from the time of diagnosis up to the time of treatment so that you feel at ease and aware of the procedures being done to you. The best possible outcomes are always our aim while at the same time ensuring that our patients suffer the least amount of discomfort and time is spent in recovery.",
        ],
    },
    {
        "slug": "laboratory-medicine", "nav_title": "Laboratory Medicine", "title": "Laboratory Medicine",
        "meta_title": "Diagnostic & Laboratory Services near Pragathi Nagar | Sree Suraksha Hospitals",
        "banner": "services/laboratory-medicine.jpg",
        "summary": "Accurate and timely diagnostic testing to support your healthcare needs.",
        "paragraphs": [
            "At Sri Suraksha Multi-specialty Hospital, our Laboratory Services are dedicated to providing accurate and timely diagnostic testing to support your healthcare needs. Our state-of-the-art laboratory is equipped with the latest technology and staffed by experienced medical technologists and pathologists who ensure the highest standards of quality and precision.",
            "We offer a comprehensive range of laboratory tests, including blood tests, urine analysis, microbiology, pathology, and genetic testing. Our commitment to excellence ensures that you receive reliable results quickly, aiding in the prompt diagnosis and effective management of various health conditions.",
            "Patient care is at the heart of our laboratory services. We prioritize your comfort and convenience, offering easy access to testing with minimal wait times. Our compassionate team is here to assist you, providing clear explanations and guidance throughout the testing process.",
        ],
    },
]

FACILITIES = [
    "General Ward A/C", "Pharmacy", "Hematology", "Clinical Pathology", "Histopathology",
    "Clinical Biochemistry", "Ultrasound", "Antenatal Scan", "Digital X Ray", "ECG", "EEG",
    "2D Echo", "TMT", "PFT", "Advanced ICU", "Advanced OT Units",
    "Laminar Air Flow & Hepa Filter", "Single Room / Sharing Room",
]
FACILITY_IMAGES = ["facilities/1.jpg", "facilities/2.jpg", "facilities/3.jpg", "facilities/4.jpg"]

DOCTORS = [
    {"name": "Dr. Divya Teja", "quals": "MBBS, DCH", "role": "Paediatrician", "img": "doctors/dr-divya-teja.jpg"},
    {"name": "Dr. Hrinath Bellamkonda", "quals": "MS (Ortho), Mch (Ortho), FIASM", "role": "Sr. Consultant Orthopedic Surgeon", "img": "doctors/dr-harinath-bellamkonda.jpg"},
    {"name": "Dr. Sanjeeva Rao K", "quals": "MBBS, DNB (Gen. Surgery), MNAMS DRNB", "role": "Vascular & Endovascular Surgeon", "img": "doctors/dr-sanjeeva-rao.jpg"},
    {"name": "Dr. Ravikishore", "quals": "MD Neuropsychiatry (Osmania), FISM (USA), CAP", "role": "Child & Adolescent Psychiatrist", "img": "doctors/dr-kishore.jpg"},
    {"name": "Dr. Manasa Chaitanya Ratna", "quals": "MS OBG", "role": "Gynecologist & Paediatrician", "img": "doctors/dr-manasa.jpg"},
    {"name": "Dr. Vishwanath", "quals": "MBBS (Gold Medalist), DNB (Gen. Surg), MNAMS, FMBS, FMAS, FIAGES, FALS", "role": "Advanced Laparoscopic & Bariatric Surgeon", "img": "doctors/dr-vishvanath.jpg"},
]

SERVICES_247 = ["Trauma Care", "Critical Care", "Pharmacy", "Lab", "Radiology", "Ambulance"]

TESTIMONIALS = [
    {"name": "Soujanya Patthi", "quote": "The staff is always warm and inviting. They are always knowledgeable, thoughtful and strive to make their patients feel welcome and comfortable. I will continue to recommend to my family and friends!"},
    {"name": "Siri J", "quote": "Admitted my son who had sudden seizures. Dr. M. Divya Teja, Pediatrician, handled him very well. She was very patient and addressed all our concerns. She advised tests only where necessary and took utmost care of our son. We are really thankful to her."},
    {"name": "Ajay Tadakara", "quote": "Excellent maintenance and very good hygiene. Had a very good consultation with the physician for me and my mother. Very detailed with lots of patience. I think the best clinic / hospital in Pragathi Nagar area."},
    {"name": "Badharinadh", "quote": "I was admitted with fever in this hospital last week, the treatment done by Dr. SVP Reddy was excellent, he doesn't encourage antibiotics or any other tests, provided fluids alone and I have recovered within 2 days. The support staff were also excellent."},
    {"name": "Saraswati", "quote": "My brother was admitted with fever in this hospital, the treatment done by Dr. SVP Reddy was excellent, he doesn't encourage antibiotics or any other tests, provided fluids alone."},
]

BLOG_POSTS = [
    {
        "slug": "best-trauma-care-centre-in-kukatpally-hyderabad",
        "title": "Best Trauma Care Centre in Kukatpally, Hyderabad",
        "meta_title": "Best Trauma Care Centre in Kukatpally Hyderabad | Sree Suraksha Hospital",
        "img": "blog/suraksha_blog_4.jpg",
        "excerpt": "Kukatpally, Hyderabad’s most crowded cities and therefore quick access to quality health care is very essential and in any event of need.",
        "paragraphs": [
            (None, "Kukatpally, Hyderabad’s most crowded cities and therefore quick access to quality health care is very essential and in any event of need. Time is precious and that is the reasons, choosing the Best Trauma Care Centre in Kukatpally may hinge on a hair’s breath. Sree Suraksha Multispeciality Hospital is one of the best clinic available in this area, which operates to provide trauma critical care and carry out critical surgery to save lives daily."),
            ("Comprehensive Trauma Care", "Injury does not select time and it’s therefore important that at the shortest time, the right medical attention be sought. Best Trauma Care Centre in Kukatpally is available at Sree Suraksha Multispeciality Hospital which holds the reputation for being one of the finest hospital with the best facilities and highly professionalised doctors. Their trauma care unit are fully equipped and can handle any kind of complicated case that may be an accident, an injury or even a medical emergency.\n\nThis institution is an actual hospital, this means that it is accessible around the clock, and the emergency services work round the clock as well. The trauma care team is made of the senior surgeons, neurologists and anesthetists willing to meet the patient’s needs so that s/he is stabilised. This makes Sree Suraksha Multispeciality Hospital the best place to find the Best Trauma Care Centre in Kukatpally."),
            ("Advanced Critical Care Services", "In addition to the best trauma center, Sree Suraksha Multispeciality Hospital is an Advanced Critical Care Hospital in Kukatpally. It refers to a high level of attention that is required before and after delivery of complicated treatment to clients with acute or chronic ailments. The intensive care unit of this hospital is ICU and has all the equipments to provide the best treatment results to the patients.\n\nThis is where Sree Suraksha Multispeciality Hospital differs from all the other hospitals because of the multiple offers in critical care. It is an inter-disciplinary group of essential critical care physicians and nurses, other health care workers who focus primarily on the independent attention of the client. It has thus developed into the most dependable Advanced Critical Care Hospital in Kukatpally through use of professionalism in the doctors and equipment."),
            ("Why Choose Sree Suraksha Multispeciality Hospital?", "The trauma and critical care facilities are part of many specialties that make this hospital the best trauma care center in Kukatpally. They have a strong framework that guarantees quick response to disasters; they also have a professional staff with a caring attitude. To ensure that all patients receive the best from the medical practitioners, the hospital has made it a policy that would ensure that the patients get the best care from the medical practitioners.\n\nBesides the traumatology & critical care, the hospital offers other specializations including the cardiology and neurology, orthopedic and other. This approach makes the hospital a hospital of choice for residents of Kukatpally and the larger community when it comes to choosing the Advanced Critical Care Hospital in Kukatpally."),
            ("Conclusion", "Sree Suraksha Multispeciality Hospital is the most preferred hospital for anyone in Kukatpally who requires an emergency treatment that could save his or her life. Being the best Trauma Care Centre in Kukatpally the hospital has the best trauma care services which meet all the emergencies. Other than that, as an Advanced Critical Care Hospital in Kukatpally area, it ensures the best possible outcomes for some of the critically ill or injured patients. Relative to trauma and critical care, hope has not left Sree Suraksha Multispeciality Hospital as the show piece of the community."),
        ],
    },
    {
        "slug": "best-neurosurgery-hospitals-in-kukatpally-hyderabad",
        "title": "Best Neurosurgery Hospital in Kukatpally, Hyderabad",
        "meta_title": "Best Neurosurgery Hospital in Kukatpally Hyderabad | Sree Suraksha Hospital",
        "img": "blog/suraksha_blog_2.jpg",
        "excerpt": "In matters concerning health especially in cases involving the nervous system, it is important to choose the right hospital and the right doctor.",
        "paragraphs": [
            (None, "In matters concerning health especially in cases involving the nervous system, it is important to choose the right hospital and the right doctor. Kukatpally, a cosmopolitan suburb in Hyderabad has come up as a medical city particularly in the field of neurosurgery, neurology and spine surgery. The best facility in this area is Suraksha Hospital which is one of the best neurosurgery hospitals in Kukatpally, Hyderabad."),
            ("Neurosurgery at Its Finest", "Neurosurgery is a complex field that deals with the diagnosis and surgical treatment of brain and spinal cord as well as peripheral nerves. Neurological disorders are on the rise and this has created a need for neurosurgeons more than ever before. The Suraksha Hospital is one of the most renowned Best neurosurgery hospitals in Kukatpally, Hyderabad, owing to its advanced technology, professional surgeons, and proper care after the surgery. From simple operations to major neurosurgery, the patients look forward to getting treated in this hospital because of the high success rate."),
            ("Expertise in Neurology", "Apart from the neurosurgery, Kukatpally has some of the Best neurologist doctors in Kukatpally Hyderabad that deals with disorders such as epilepsy, stroke, multiple sclerosis, and Parkinson’s disease. This hospital has been reputed for its professional neurologists who are dedicated to offering the best solutions to the patients. The most qualified the Best neurologist doctors in Kukatpally, Hyderabad are in Suraksha Hospital where they use modern and accurate diagnostic equipment to diagnose and treat the patients.\n\nNeurological diseases require constant attention and having a team of doctors in one healthcare center makes it easier for patients to get the attention they need. Right from the time of diagnosis to the time of rehabilitation, Suraksha Hospital is one of the well-known hospitals in the area which provides neurological care."),
            ("Spine Surgery Excellence", "Spine related conditions are among the most disabling as they restrict one’s mobility and even ability to enjoy life. There are the best spine surgeons in Kukatpally, Hyderabad to treat spine issues including herniated disc, spine deformity, and other diseases affecting the spine. Best spine surgeons in Kukatpally, Hyderabad are the most qualified and experienced to perform the spine surgeries through open and endoscopic techniques.\n\nPatients experiencing chronic back pain, sciatica, or spinal injuries can find relief through the advanced surgical options available here. The hospital's spine surgery department is known for its patient-centered approach, ensuring that every patient receives the most effective treatment tailored to their unique condition."),
            ("Conclusion", "For anyone seeking top-tier neurological and spine care, Suraksha Hospital stands out as the best choice in Kukatpally. Whether you are looking for the best neurosurgery hospital in Kukatpally, Hyderabad, the best neurologist doctors in Kukatpally, Hyderabad, or the best spine surgeon in Kukatpally, Hyderabad, Suraksha Hospital delivers on all fronts."),
        ],
    },
    {
        "slug": "best-orthopedic-hospital-in-kukatpally-hyderabad",
        "title": "Best Orthopedic Hospital in Kukatpally, Hyderabad",
        "meta_title": "Best Orthopedic Hospital in Kukatpally Hyderabad | Sree Suraksha Hospital",
        "img": "blog/suraksha_blog_1.jpg",
        "excerpt": "In regard to the management of knee pain and other orthopedic conditions, the choice of a healthcare center and a doctor is critical.",
        "paragraphs": [
            (None, "In regard to the management of knee pain and other orthopedic conditions, the choice of a healthcare center and a doctor is critical. Hyderabad has many healthcare facilities, and among them, Suraksha Hospital is one of the best places for orthopedic treatment located in Kukatpally. This is why it is acknowledged as the best orthopedic hospital in Kukatpally Hyderabad and why it houses some of the best orthopedic doctors in Hyderabad particularly for knee pain."),
            ("Comprehensive Orthopedic Care", "The services provided by Suraksha Hospital in the orthopedic field are extensive and cover all the needs of the patients. Starting from diagnosis, through treatment and up to the rehabilitation, the hospital offers complex care for orthopedic disorders. The facility is well equipped with modern equipment to enable accurate diagnosis and proper treatment of the clients."),
            ("Expertise in Knee Pain Management", "Knee pain is one of the most prevalent complaints in people of all ages and to treat it, one needs to take into consideration certain factors. Over the years, Suraksha Hospital has become well-known for the effective treatment of knee pain due to the orthopedic doctors who are skilled in the modern techniques of treatment. Whether the knee pain is because of arthritis, ligament injuries, or other issues, the team of knee specialists at Suraksha Hospital develops appropriate treatment plans with the goal of reducing pain and improving the quality of the patient’s life."),
            ("Renowned Orthopedic Specialists", "This is an essential aspect that makes Suraksha Hospital stand out from other hospitals because of the Best Orthopedic Doctor in Hyderabad for Knee pain. These people are experienced and devoted to delivering the highest quality of care to their patients. The hospital has hired qualified orthopedic doctors with adequate experience and who have the best interest of the patients in mind."),
            ("Advanced Surgical Techniques", "In situations that require surgery, Suraksha Hospital uses modern surgical procedures that focus on the patient’s safety and healing process. Arthroscopy is done frequently as a minimally invasive surgery to treat knee injuries and patients are able to get back to their normal activities with little pain within a short period."),
            ("Personalized Rehabilitation Programs", "Rehabilitation after the treatment is equally important in orthopedic care and Suraksha Hospital also offers the best rehabilitation services. The hospital has individualized rehabilitation services that are aimed at helping the patient to regain strength, get back on their feet and get back to their normal lives as soon as possible."),
            ("Patient-Centered Approach", "The major strength that sets Suraksha Hospital apart from the rest is the focus on patients. The patient care delivery system adopted in the hospital guarantees that the needs of each patient as well as his or her concerns are well attended to in a professional manner."),
            ("Conclusion", "Suraksha Hospital is the best orthopedic hospital Kukatpally Hyderabad because of the hospital’s comprehensive services, highly skilled doctors, modern surgical procedures, and tailored rehabilitation services. If you are looking for the best orthopedic doctor in Hyderabad for knee pain, then Suraksha Hospital is the right place for you to get the best treatment with a friendly approach."),
        ],
    },
    {
        "slug": "best-joint-replacement-doctors-in-kukatpally-hyderabad",
        "title": "Best Joint Replacement Doctors In Kukatpally Hyderabad",
        "meta_title": "Best Joint Replacement Doctors In Kukatpally Hyderabad | Sree Suraksha Hospital",
        "img": "blog/suraksha_blog_3.jpg",
        "excerpt": "Arthritis affects the joints and this makes it difficult to carry out simple activities as if one is facing a lot of resistance.",
        "paragraphs": [
            (None, "Arthritis affects the joints and this makes it difficult to carry out simple activities as if one is facing a lot of resistance. With the constant development in technology, joint replacement surgeries have been a revolutionary solution for those with severe joint problems. Sree Suraksha Hospital situated in Kukatpally, Hyderabad is famous for providing advanced treatment for joint replacement especially robotic assisted surgery that is more accurate and has better results for patients. In case you are looking for the Best joint replacement doctors in Kukatpally Hyderabad, this hospital should be your top choice."),
            ("Expert Joint Replacement Surgeons at Sree Suraksha Hospital", "Knee and hip replacements are among the most delicate surgeries that need the hands of a surgeon who is well experienced. Best joint replacement doctors in Kukatpally Hyderabad at Sree Suraksha Hospital are very experienced and dedicated to provide the best treatment to all the patients. These specialists have a vast experience in performing the surgery and they are fully conversant with modern and complex surgery to enable patients to have a smooth recovery process."),
            ("Revolutionizing Knee Surgery with Robotic Technology", "Knee replacement surgery is usually performed on patients with chronic knee pain or those who have a degenerative disease of the knee joint such as arthritis. In Sree Suraksha Hospital, they have recently introduced the Robotic knee replacement surgery in Hyderabad which has changed the way the knee replacements are done. Robot assisted surgeries are beneficial than the conventional techniques in that they are accurate, invasive and have short recovery period."),
            ("Why Choose Sree Suraksha Hospital for Hip Replacement?", "Another common operation is the hip replacement which can help patients with hip joint problems to regain their ability to move and get rid of pain that has been bothering them for a long time. Sree Suraksha Hospital is the place where the Best hip replacement surgeon in Kukatpally operates and offers full support to the patients, including physiotherapy."),
            ("Personalized Care from Consultation to Recovery", "One more feature that can be distinguished in Sree Suraksha Hospital is the fact that it is a patient oriented hospital. From the time the patient is first seen and advised to undergo surgery to the time the patient is taken through physiotherapy after the surgery is done, the hospital’s team ensures that the process is personalized."),
            ("Achieving the Best Outcomes in Joint Replacement", "The thing that makes Sree Suraksha Hospital stand out is the focus on the best results in the field of medicine with the help of modern equipment and professional staff. Be it robotic knee replacement surgery in Hyderabad or the best hip replacement surgeon in Kukatpally, this hospital makes sure that the patient gets the best treatment possible.\n\nTherefore, for anyone requiring joint replacement surgery, Sree Suraksha Hospital presents the best opportunity through the best joint replacement surgeons in Kukatpally Hyd."),
        ],
    },
]

ASSET = "/assets/original-site/images/"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def icon_phone():
    return '<svg viewBox="0 0 24 24" width="18" height="18" fill="none"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.9 21 3 13.1 3 3c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1L6.6 10.8z" fill="currentColor"/></svg>'


def icon_mail():
    return '<svg viewBox="0 0 24 24" width="18" height="18" fill="none"><path d="M3 5h18a1 1 0 011 1v12a1 1 0 01-1 1H3a1 1 0 01-1-1V6a1 1 0 011-1z" stroke="currentColor" stroke-width="1.8"/><path d="M2.5 6.5l9.5 7 9.5-7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def icon_pin():
    return '<svg viewBox="0 0 24 24" width="18" height="18" fill="none"><path d="M12 22s7-7.4 7-13a7 7 0 10-14 0c0 5.6 7 13 7 13z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="9" r="2.5" stroke="currentColor" stroke-width="1.8"/></svg>'


def icon_social(name):
    icons = {
        "facebook": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M13.5 21v-7.5H16l.5-3H13.5V8.4c0-.87.24-1.46 1.5-1.46H16.6V4.3C16.3 4.26 15.3 4.17 14.14 4.17c-2.4 0-4.04 1.46-4.04 4.15v2.35H7.6v3h2.5V21h3.4z"/></svg>',
        "twitter": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M18.9 3H21l-6.6 7.6L22.2 21h-6.9l-5.4-6.6L3.7 21H1.6l7.1-8.1L1 3h7l4.9 6 6-6zm-1.2 16.2h1.9L7.4 4.7H5.4l12.3 14.5z"/></svg>',
        "instagram": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 8.5a3.5 3.5 0 100 7 3.5 3.5 0 000-7zM12 2c-2.7 0-3.06.01-4.12.06-1.06.05-1.79.22-2.43.47-.66.26-1.22.6-1.77 1.16-.55.55-.9 1.11-1.16 1.77-.25.64-.42 1.37-.47 2.43C2 8.94 2 9.3 2 12s.01 3.06.06 4.12c.05 1.06.22 1.79.47 2.43.26.66.6 1.22 1.16 1.77.55.55 1.11.9 1.77 1.16.64.25 1.37.42 2.43.47C8.94 22 9.3 22 12 22s3.06-.01 4.12-.06c1.06-.05 1.79-.22 2.43-.47.66-.26 1.22-.6 1.77-1.16.55-.55.9-1.11 1.16-1.77.25-.64.42-1.37.47-2.43.05-1.06.06-1.42.06-4.12s-.01-3.06-.06-4.12c-.05-1.06-.22-1.79-.47-2.43a4.9 4.9 0 00-1.16-1.77 4.9 4.9 0 00-1.77-1.16c-.64-.25-1.37-.42-2.43-.47C15.06 2.01 14.7 2 12 2zm0 3.8a6.2 6.2 0 110 12.4 6.2 6.2 0 010-12.4zm6.4-.5a1.4 1.4 0 11-2.8 0 1.4 1.4 0 012.8 0z"/></svg>',
        "linkedin": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M6.94 8.5H3.56V21h3.38V8.5zM5.25 3a1.96 1.96 0 100 3.92A1.96 1.96 0 005.25 3zM20.45 21h-3.37v-6.44c0-1.53-.03-3.5-2.13-3.5-2.14 0-2.47 1.67-2.47 3.4V21H9.1V8.5h3.24v1.7h.05c.45-.85 1.56-1.75 3.2-1.75 3.42 0 4.06 2.25 4.06 5.18V21z"/></svg>',
        "youtube": '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M23 12s0-3.4-.43-5a2.9 2.9 0 00-2-2C18.9 4.5 12 4.5 12 4.5s-6.9 0-8.57.5a2.9 2.9 0 00-2 2C1 8.6 1 12 1 12s0 3.4.43 5a2.9 2.9 0 002 2c1.67.5 8.57.5 8.57.5s6.9 0 8.57-.5a2.9 2.9 0 002-2C23 15.4 23 12 23 12zM9.8 15.5v-7l6.2 3.5-6.2 3.5z"/></svg>',
    }
    return icons.get(name, "")


def render_head(meta_title, meta_desc, canonical_path):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(meta_title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="https://sreesurakshapragathinagar.pages.dev{canonical_path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
<link rel="icon" type="image/png" href="{ASSET}logo.png">
"""


def render_header(active_path):
    phones_display = ", ".join(SITE["phones"])
    nav_html = "\n".join(
        f'      <a href="{href}" class="navbar__link{" is-active" if href == active_path else ""}">{label}</a>'
        for label, href in NAV_LINKS
    )
    return f"""<div class="top-strip">
  <div class="container top-strip__inner">
    <div class="top-strip__contacts">
      <a href="mailto:{SITE['email']}" class="top-strip__link">{icon_mail()}<span>{SITE['email']}</span></a>
      <a href="tel:{SITE['phone_href']}" class="top-strip__link">{icon_phone()}<span>{phones_display}</span></a>
    </div>
    <div class="top-strip__social">
      <a href="{SITE['social']['facebook']}" target="_blank" rel="noopener">{icon_social('facebook')}</a>
      <a href="{SITE['social']['twitter']}" target="_blank" rel="noopener">{icon_social('twitter')}</a>
      <a href="{SITE['social']['instagram']}" target="_blank" rel="noopener">{icon_social('instagram')}</a>
      <a href="{SITE['social']['linkedin']}" target="_blank" rel="noopener">{icon_social('linkedin')}</a>
      <a href="{SITE['social']['youtube']}" target="_blank" rel="noopener">{icon_social('youtube')}</a>
    </div>
  </div>
</div>

<header class="navbar" id="navbar">
  <div class="container navbar__inner">
    <a href="/" class="navbar__logo">
      <img src="{ASSET}logo.png" alt="{SITE['full_name']}" class="navbar__logo-img">
    </a>
    <nav class="navbar__nav" id="primaryNav">
{nav_html}
    </nav>
    <div class="navbar__call">
      <span class="navbar__call-icon">{icon_phone()}</span>
      <span class="navbar__call-text">Call Now<strong>{SITE['phones'][0]}</strong></span>
    </div>
    <a href="/book-an-appointment/" class="btn btn--primary">Book An Appointment</a>
    <button class="navbar__toggle" id="navToggle" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="primaryNav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""


def render_footer():
    quick_html = "\n".join(f'        <a href="{href}">{label}</a>' for label, href in FOOTER_QUICK_LINKS)
    service_html = "\n".join(f'        <a href="{href}">{label}</a>' for label, href in FOOTER_SERVICE_LINKS)
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__about">
        <img src="{ASSET}logo.png" alt="{SITE['full_name']}" class="footer__logo-img">
        <p>{SITE['full_name']} ({SITE['unit_of']}) is committed to providing quality, patient-centered multispeciality healthcare in Pragathi Nagar, Kukatpally, Hyderabad &mdash; with 24/7 trauma, critical care, and emergency services.</p>
        <div class="footer__social">
          <a href="{SITE['social']['facebook']}" target="_blank" rel="noopener">{icon_social('facebook')}</a>
          <a href="{SITE['social']['twitter']}" target="_blank" rel="noopener">{icon_social('twitter')}</a>
          <a href="{SITE['social']['instagram']}" target="_blank" rel="noopener">{icon_social('instagram')}</a>
          <a href="{SITE['social']['linkedin']}" target="_blank" rel="noopener">{icon_social('linkedin')}</a>
          <a href="{SITE['social']['youtube']}" target="_blank" rel="noopener">{icon_social('youtube')}</a>
        </div>
      </div>
      <div class="footer__links">
        <h3>Quick Links</h3>
{quick_html}
      </div>
      <div class="footer__links">
        <h3>Services</h3>
{service_html}
      </div>
      <div>
        <h3>Useful Links</h3>
        <ul class="footer__contact">
          <li><span class="ico">{icon_pin()}</span><span>{SITE['address']}</span></li>
          <li><span class="ico">{icon_phone()}</span><span>{", ".join(SITE['phones'])}</span></li>
          <li><span class="ico">{icon_mail()}</span><span>{SITE['email']}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p>&copy; {2024} {SITE['name']}. All Rights Reserved.</p>
    </div>
  </div>
</footer>

<a href="#top" class="back-to-top" id="backToTop" aria-label="Back to top">
  <svg viewBox="0 0 24 24" width="20" height="20" fill="none"><path d="M12 19V5M5 12l7-7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
</a>
<a href="tel:{SITE['phone_href']}" class="floating-call" aria-label="Call now">{icon_phone()}</a>

<script src="/js/main.js"></script>
"""


def page_shell(meta_title, meta_desc, canonical_path, active_path, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head(meta_title, meta_desc, canonical_path)}</head>
<body id="top">
{render_header(active_path)}
<main>
{body_html}
</main>
{render_footer()}
</body>
</html>
"""


def page_header_block(title, crumbs):
    crumb_html = " &rsaquo; ".join(
        f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>"
        for label, href in crumbs
    )
    return f"""  <section class="page-header">
    <div class="container">
      <h1>{esc(title)}</h1>
      <div class="page-header__crumbs">{crumb_html}</div>
    </div>
  </section>
"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def render_department_body(dept):
    if "conditions" in dept:
        paras = "".join(f"<p>{esc(p)}</p>" for p in dept["paragraphs"])
        items = "".join(
            f'<div class="condition-list__item"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
            for h, p in dept["conditions"]
        )
        return paras + f'<div class="condition-list">{items}</div>'
    if "paragraphs_headed" in dept:
        out = []
        for h, p in dept["paragraphs_headed"]:
            if h:
                out.append(f"<h2>{esc(h)}</h2>")
            out.append(f"<p>{esc(p)}</p>")
        return "".join(out)
    return "".join(f"<p>{esc(p)}</p>" for p in dept["paragraphs"])


def sidebar_html(current_slug=None):
    items = "".join(
        f'<li><a href="/{d["slug"]}/">{esc(d["nav_title"])}</a></li>'
        for d in DEPARTMENTS
    )
    return f"""<aside>
        <div class="sidebar-card">
          <h4>All Departments</h4>
          <ul>{items}</ul>
        </div>
        <div class="sidebar-card sidebar-card--cta">
          <h4>Need Immediate Care?</h4>
          <p>24/7 trauma &amp; emergency services available.</p>
          <a href="tel:{SITE['phone_href']}" class="btn btn--light btn--block">Call {SITE['phones'][0]}</a>
        </div>
      </aside>"""


def build_department_page(dept):
    body = f"""{page_header_block(dept['title'], [("Home", "/"), ("Services", "/our-services/"), (dept['title'], None)])}
  <section class="content-page">
    <div class="container content-page__grid">
      <div class="content-page__body">
        <img src="{ASSET}{dept['banner']}" alt="{esc(dept['title'])}" class="content-page__banner" style="margin-bottom:28px;">
        <h2>{esc(dept['title'])}</h2>
        {render_department_body(dept)}
      </div>
      {sidebar_html(dept['slug'])}
    </div>
  </section>
"""
    html = page_shell(dept["meta_title"], dept["summary"], f"/{dept['slug']}/", None, body)
    write(f"{dept['slug']}/index.html", html)


def build_home():
    service_cards = "".join(f"""
      <article class="service-card">
        <div class="service-card__img"><img src="{ASSET}{s['img']}" alt="{esc(s['title'])}" loading="lazy"></div>
        <div class="service-card__body">
          <h3>{esc(s['title'])}</h3>
          <p>{esc(s['desc'])}</p>
          <a href="/{s['slug']}/" class="service-card__link">Read More &rarr;</a>
        </div>
      </article>""" for s in HOME_SERVICES)

    half = len(FACILITIES) // 2 + len(FACILITIES) % 2
    col1 = FACILITIES[:half]
    col2 = FACILITIES[half:]
    facility_cards = ""
    cols = [(FACILITY_IMAGES[0], col1), (FACILITY_IMAGES[1], col2)]
    for img, items in cols:
        li = "".join(f"<li>{esc(i)}</li>" for i in items)
        facility_cards += f"""
      <div class="facility-card">
        <img src="{ASSET}{img}" alt="Hospital facility" loading="lazy">
        <ul class="facility-card__list">{li}</ul>
      </div>"""

    doctor_cards = "".join(f"""
      <div class="doctor-card">
        <div class="doctor-card__photo"><img src="{ASSET}{d['img']}" alt="{esc(d['name'])}" loading="lazy"></div>
        <h3>{esc(d['name'])}</h3>
        <p class="doctor-card__quals">{esc(d['quals'])}</p>
        <p class="doctor-card__role">{esc(d['role'])}</p>
      </div>""" for d in DOCTORS)

    strip_items = "".join(f'<div class="strip247__item"><strong>{esc(s)}</strong><span>24/7 Available</span></div>' for s in SERVICES_247)

    testimonial_cards = "".join(f"""
      <div class="testimonial-card">
        <p class="testimonial-card__quote">&ldquo;{esc(t['quote'])}&rdquo;</p>
        <div class="testimonial-card__author">
          <img src="{ASSET}profile.jpg" alt="{esc(t['name'])}" loading="lazy">
          <strong>{esc(t['name'])}</strong>
        </div>
      </div>""" for t in TESTIMONIALS)

    body = f"""
  <section class="hero">
    <div class="hero__media">
      <video autoplay muted loop playsinline poster="{ASSET}services/services-1.jpg">
        <source src="/assets/original-site/video/video-1.mp4" type="video/mp4">
      </video>
      <div class="hero__scrim"></div>
      <div class="hero__content">
        <div class="container">
          <p class="hero__eyebrow">Your Health, Our Priority</p>
          <h1 class="hero__title">{esc(SITE['full_name'])}</h1>
          <p class="hero__subtitle">The best way to predict the future is to create it. 24/7 emergency, trauma &amp; multispeciality care in Pragathi Nagar, Hyderabad.</p>
          <div class="hero__actions">
            <a href="/book-an-appointment/" class="btn btn--primary">Book An Appointment</a>
            <a href="tel:{SITE['phone_href']}" class="btn btn--outline" style="background:#fff;">Call Now</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">What We Offer</p>
        <h2 class="section-title">Our Services</h2>
      </div>
      <div class="services-grid">{service_cards}
      </div>
      <div class="section-cta"><a href="/our-services/" class="btn btn--outline">View All Services</a></div>
    </div>
  </section>

  <section class="section--alt">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Infrastructure</p>
        <h2 class="section-title">Our Facilities</h2>
      </div>
      <div class="facilities-grid">{facility_cards}
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Our Specialists</p>
        <h2 class="section-title">Our Doctors</h2>
      </div>
      <div class="doctors-grid">{doctor_cards}
      </div>
    </div>
  </section>

  <section class="strip247">
    <div class="container">
      <div class="section-head" style="margin-bottom:26px;">
        <p class="eyebrow" style="color:#f5821f;">Round The Clock</p>
        <h2 class="section-title" style="color:#fff;">Our 24/7 Services</h2>
      </div>
      <div class="strip247__grid">{strip_items}
      </div>
    </div>
  </section>

  <section class="section--alt">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Testimonials</p>
        <h2 class="section-title">What Our Patients Say</h2>
      </div>
      <div class="testimonials-grid">{testimonial_cards}
      </div>
    </div>
  </section>
"""
    html = page_shell(
        "Best Multispecialty Hospital in Pragathi Nagar | Sree Suraksha",
        "Sree Suraksha Multispeciality Hospital, Pragathi Nagar, Hyderabad — 24/7 trauma & critical care, general medicine, orthopaedics, paediatrics, diabetology and more.",
        "/", "/", body,
    )
    write("index.html", html)


def build_our_services():
    cards = "".join(f"""
      <article class="service-card">
        <div class="service-card__img"><img src="{ASSET}{d['banner']}" alt="{esc(d['title'])}" loading="lazy"></div>
        <div class="service-card__body">
          <h3>{esc(d['title'])}</h3>
          <p>{esc(d['summary'])}</p>
          <a href="/{d['slug']}/" class="service-card__link">Read More &rarr;</a>
        </div>
      </article>""" for d in DEPARTMENTS)
    body = f"""{page_header_block("Our Services", [("Home", "/"), ("Our Services", None)])}
  <section>
    <div class="container">
      <div class="services-listing">{cards}
      </div>
    </div>
  </section>
"""
    html = page_shell(
        "Our Services | Sree Suraksha Multispeciality Hospital",
        "Explore all clinical departments at Sree Suraksha Multispeciality Hospital, Pragathi Nagar — from general medicine to neurosurgery and oncology.",
        "/our-services/", "/our-services/", body,
    )
    write("our-services/index.html", html)


def build_blog_index():
    cards = "".join(f"""
      <article class="blog-card">
        <div class="blog-card__img"><a href="/{p['slug']}/"><img src="{ASSET}{p['img']}" alt="{esc(p['title'])}" loading="lazy"></a></div>
        <div class="blog-card__body">
          <h3><a href="/{p['slug']}/">{esc(p['title'])}</a></h3>
          <p>{esc(p['excerpt'])}</p>
          <a href="/{p['slug']}/" class="service-card__link">Read More &rarr;</a>
        </div>
      </article>""" for p in BLOG_POSTS)
    body = f"""{page_header_block("Blog", [("Home", "/"), ("Blog", None)])}
  <section>
    <div class="container">
      <div class="blog-grid">{cards}
      </div>
    </div>
  </section>
"""
    html = page_shell(
        "Blog | Sree Suraksha Multispeciality Hospital",
        "Health articles and hospital updates from Sree Suraksha Multispeciality Hospital, Pragathi Nagar, Hyderabad.",
        "/blog/", "/blog/", body,
    )
    write("blog/index.html", html)


def build_blog_post(post):
    paras = []
    for h, text in post["paragraphs"]:
        if h:
            paras.append(f"<h2>{esc(h)}</h2>")
        for chunk in text.split("\n\n"):
            paras.append(f"<p>{esc(chunk)}</p>")
    body = f"""{page_header_block(post['title'], [("Home", "/"), ("Blog", "/blog/"), (post['title'], None)])}
  <section class="content-page">
    <div class="container content-page__grid">
      <div class="content-page__body">
        <img src="{ASSET}{post['img']}" alt="{esc(post['title'])}" class="content-page__banner" style="margin-bottom:28px;">
        {''.join(paras)}
      </div>
      {sidebar_html()}
    </div>
  </section>
"""
    html = page_shell(post["meta_title"], post["excerpt"], f"/{post['slug']}/", None, body)
    write(f"{post['slug']}/index.html", html)


def build_contact():
    body = f"""{page_header_block("Contact Us", [("Home", "/"), ("Contact Us", None)])}
  <section>
    <div class="container contact-grid">
      <div>
        <div class="section-head" style="text-align:left; margin:0 0 24px;">
          <p class="eyebrow">Get In Touch</p>
          <h2 class="section-title">We're Here To Help</h2>
        </div>
        <div class="contact-cards">
          <div class="contact-card">
            <span class="contact-card__icon">{icon_pin()}</span>
            <div><h4>Address</h4><p>{SITE['address']}</p></div>
          </div>
          <div class="contact-card">
            <span class="contact-card__icon">{icon_phone()}</span>
            <div><h4>Phone</h4><p>{"<br>".join(SITE['phones'])}</p></div>
          </div>
          <div class="contact-card">
            <span class="contact-card__icon">{icon_mail()}</span>
            <div><h4>Email</h4><p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p></div>
          </div>
        </div>
        <div class="map-frame">
          <iframe title="Hospital location map" src="{SITE['map_embed']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
      </div>
      <div class="form-card">
        <div class="form-success">Thanks! Your message is ready to send &mdash; please confirm in your email app.</div>
        <form data-lead-form>
          <div class="form-row">
            <div class="form-field"><label for="cName">Your Name</label><input id="cName" name="name" type="text" required></div>
            <div class="form-field"><label for="cEmail">Your Email</label><input id="cEmail" name="email" type="email" required></div>
          </div>
          <div class="form-row">
            <div class="form-field"><label for="cPhone">Your Phone</label><input id="cPhone" name="phone" type="tel" required></div>
            <div class="form-field"><label for="cSubject">Subject</label><input id="cSubject" name="subject" type="text"></div>
          </div>
          <div class="form-row form-row--full">
            <div class="form-field"><label for="cMessage">Your Message</label><textarea id="cMessage" name="message" rows="5" required></textarea></div>
          </div>
          <button type="submit" class="btn btn--primary btn--block">Send Message</button>
          <p class="form-note">This form opens your email app with the message pre-filled. To receive submissions directly, connect a form backend (see README).</p>
        </form>
      </div>
    </div>
  </section>
"""
    html = page_shell(
        "Contact Us | Sree Suraksha Multispeciality Hospital",
        "Get in touch with Sree Suraksha Multispeciality Hospital, Pragathi Nagar, Hyderabad. Call, email, or visit us.",
        "/contact-us/", "/contact-us/", body,
    )
    write("contact-us/index.html", html)


def build_book_appointment():
    body = f"""{page_header_block("Book an Appointment", [("Home", "/"), ("Book an Appointment", None)])}
  <section>
    <div class="container" style="max-width:760px;">
      <div class="form-card">
        <div class="form-success">Thanks! Your appointment request is ready to send &mdash; please confirm in your email app.</div>
        <form data-lead-form>
          <div class="form-row">
            <div class="form-field"><label for="aName">Name</label><input id="aName" name="name" type="text" required></div>
            <div class="form-field"><label for="aEmail">Email Address</label><input id="aEmail" name="email" type="email" required></div>
          </div>
          <div class="form-row">
            <div class="form-field"><label for="aPhone">Phone Number</label><input id="aPhone" name="phone" type="tel" required></div>
            <div class="form-field"><label for="aDate">Preferred Date</label><input id="aDate" name="date" type="date" required></div>
          </div>
          <div class="form-row form-row--full">
            <div class="form-field"><label for="aMessage">Message</label><textarea id="aMessage" name="message" rows="5" placeholder="Tell us which department or doctor you'd like to see"></textarea></div>
          </div>
          <button type="submit" class="btn btn--primary btn--block">Submit</button>
          <p class="form-note">This form opens your email app with the request pre-filled. To receive submissions directly, connect a form backend (see README).</p>
        </form>
      </div>
    </div>
  </section>
"""
    html = page_shell(
        "Book an Appointment | Sree Suraksha Multispeciality Hospital",
        "Book your appointment today at Sree Suraksha Multispeciality Hospital, Pragathi Nagar, Hyderabad.",
        "/book-an-appointment/", "/book-an-appointment/", body,
    )
    write("book-an-appointment/index.html", html)


def main():
    build_home()
    build_our_services()
    build_blog_index()
    build_contact()
    build_book_appointment()
    for dept in DEPARTMENTS:
        build_department_page(dept)
    for post in BLOG_POSTS:
        build_blog_post(post)
    print("Generated", 5 + len(DEPARTMENTS) + len(BLOG_POSTS), "pages.")


if __name__ == "__main__":
    main()
