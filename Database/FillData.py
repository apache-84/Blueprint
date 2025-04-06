import sqlite3
import hashlib

DB_FILE = "../Database/blueprintdb.db"
# (courseID, courseName, description, recommendHours, courseDifficulty, sections, reccommendedYear, term)
def insert():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Courses dummy data
    cursor.executemany("""
            INSERT INTO Courses 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, [
                ('CSCI 112','Applications Programming','An introduction to the use and customization of application packages. Includes macro programming as well as visual programming.', 0, 0,'All Sections', 1,'Both'),
                ('CSCI 115','Introduction to Web Page Development ','An introduction to Web page construction for students not majoring in Computer Science. The course focuses on client-side techniques: Hypertext Markup Language (HTML, XHTML), Cascading Style Sheets (CSS), and an introduction to JavaScript. Computer Science students may take this course for credit towards their major in Computer Science. ', 0, 0,'All Sections',1,'Both'),
                ('CSCI 159','Computer Sciece I','A first year course in computer science. Topics include structured programming, top-down program design, procedures, recursion, and an introduction to dynamic data structures.', 0, 0,'All Sections', 1,'Both'),
                ('CSCI 160','Computer Science I for Engineering','A first year course in computer science. Topics include structured programming, top-down program design, procedures, recursion, and an introduction to dynamic data structures.', 0, 0,'All Sections', 1,'Both'),
                ('CSCI 161','Computer Science II','Topics include an introduction to objects, classes, object-oriented programming techniques (encapsulation, inheritance, and polymorphism), dynamic data structures (dynamic arrays, linked lists and trees), and abstract data types (stacks, queues and dictionaries).', 0, 0,'All Sections', 1,'Both'),
                ('CSCI 162','Topics in Computer Science','An introduction to applied and theoretical topics, designed to develop an understanding of key concepts in computer science. Topics include digital logic, programming language paradigms including logic and functional programming, computer organization and architecture, system software, software engineering principles, and theory of computation.', 0, 0,'All Sections', 1,'Both'),
                ('CSCI 251','Systems and Networks','An introduction to operating systems and computer networks. Topics include network architectures, communications protocols, client / server architecture and file systems. The lab component includes hardware and software installations, upgrades and backups.', 0, 0,'All Sections', 2,'Both'),
                ('CSCI 260','Data Structures','An examination of various methods of representing and manipulating data, including internal representation of data, stacks, queues, linked lists, trees and graphs. Analysis of algorithms will also be discussed extensively. ', 0, 0,'All Sections', 2,'Both'),
                ('CSCI 261','Computer Architecture & Assembly Language ','An introduction to computer organization, and machine and assembly languages. Topics include data representation, the instruction set and addressing modes of a chosen processor, procedures and parameter passing, and the use of operating system services.', 0, 0,'All Sections', 2,'Both'),
                ('CSCI 265','Software Engineering','An exploration of the methods and tools for developing high quality software. The course includes topics in program design, program style, algorithm selection, interface design, debugging and testing, system utilities, version control, regular expressions and an introduction to scripting languages.', 0, 0,'All Sections', 2,'Both'),
                ('CSCI 301','Introduction to the Practice of Cyber-Security ','An introduction to key cyber-security concepts as applied to information systems in a business environment. Topics include assessing risk in cyber-security, attack vectors, tenets of cyber-security, the human element, operation security, application security, mobile and IoT security, and incident response plans.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 307','Preparation for Co-operative Education Employment','Preparation for first co-operative education experience through practical training in areas such as resume writing and interview skills.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 308','Co-operative Work Placement I','Individual students are carefully matched to employers who supervise them and evaluate their performance during paid work experience. University personnel conduct monitoring. Students will write a work placement report.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 309','Co-operative Work Placement II ','The second work placement, as described for CSCI 308', 0, 0,'All Sections',3,'Both'),
                ('CSCI 310','Introduction to Human-Computer Interaction ','An introduction to understanding human behaviour as it applies to interface design, implementation, and evaluation. Topics include: design issues and goals, the limits of the human cognitive system, user-centered design, prototyping, establishing requirements, evaluation techniques, and design implications of emerging technologies. ', 0, 0,'All Sections',3,'Both'),
                ('CSCI 311','Web Programming','Exploration of languages, tools and techniques to write software for use within the World Wide Web (WWW). The course includes the WWW client/server model and related protocols, web server properties, web markup languages, client/server scripting tools, server side programming, and database access tools.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 320','Foundations of Computer Science ','A survey of formal models and results that form the theoretical foundation of computer science. Typical topics include finite automata, Turing machines, simple undecidable problems, context-free languages, grammars and elementary computational complexity.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 330','Programming Languages','The fundamental concepts of imperative and applicative programming languages. Topics include the description of data types, variable assignment and sharing, sequencing, iteration and recursion, parameter passing mechanisms, and type checking.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 331','Object-Oriented Software Development ','Topics include aspects of object-oriented analysis, design and development; definition and comparison of object-oriented metrics; verification methods for OO-software; maintenance and reuse issues.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 355','Digital Logic and Computer Organization','The fundamentals of logic design, computer organization, and the structure of major hardware components of computers. Topics include the application of Boolean algebra to switching circuits; the use of MSI, LSI and field programmable devices in digital design; combinatorial and sequential circuits, flip flops, counters, memory organization, CAD tools.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 360','Intro to Operating Systems','An introduction to the major concepts of operating systems and study of the interrelationships between the operating system and the architecture of computer systems. Topics include operating system structures, concurrent programming techniques, cpu scheduling, deadlocks, memory management, file systems and protection. ', 0, 0,'All Sections',3,'Both'),
                ('CSCI 370','Database Systems ','An introduction to the use and operating principles of database management systems. Topics include data entities and relationships, data modelling using Entity-Relationship Diagrams, hierarchical, network and relational models of databases, query language, physical representation of data in secondary storage, relational algebra and calculus as applied to the design of databases, security and integrity in the context of concurrent use, and basic ethical issues associated with database design and use.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 375','Intro to Systems Analysis ','The methods and methodologies used in analyzing and designing various types of systems. Topics include project definition, CASE tools, data gathering, structured analysis and design, human-machine interface, database design, system controls, hardware selection and system testing, implementation and operation. Students are assigned to a project team involved in a system study as part of the course.', 0, 0,'All Sections',3,'Both'),
                ('CSCI 400','Computers and Society','An introduction to the social, philosophical and ethical issues of technology with an emphasis on computing technology. Topics covered include privacy, social control, information, the changing nature of work and appropriate technology. ', 0, 0,'All Sections',4,'Both'),
                ('CSCI 405','Computer Graphics ','The fundamental algorithms and data structures used in generative computer graphics. Topics include structure of interactive graphics programs, raster algorithms, colour, two- and three-dimensional geometric transformations, animation, parallel and perspective projection, hidden line and hidden surface algorithms, cubic curves and surfaces, and shading models. Optional topics include fractals/L-systems, and GPU hardware programming.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 408','Co-operative Work Placement III ','The third work placement, as described for CSCI 308.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 409','Co-operative Work Placement IV ','A survey of advanced topics in algorithm design and analysis. Typical topics include complexity analysis, strategies for intractable problems, approximation algorithms, random algorithms, advanced data structures for sorting and searching, graph and network algorithms, amortized analysis. ', 0, 0,'All Sections',4,'Both'),
                ('CSCI 422','Advanced Algorithms ','This course examines selected emerging and advanced topics in Algorithms and Complexity Theory. Topics may include: advanced techniques for algorithm analysis; complexity classes; algorithmic techniques in graph theory, combinatorics, and optimization; approximation algorithms; distributed and parallel algorithms; probabilistic algorithms; online algorithms; quantum algorithms. May be taken more than once in different topics with permission of Department Chair. CSCI 429 was formerly called CSCI 485C; credit will not be granted for both courses.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 429','Advanced Topics in Algorithms and Complexity ','desc', 0, 0,'All Sections',4,'Both'),
                ('CSCI 439','Advanced Topics in Programming ','This course examines selected emerging and advanced topics in programming. Topics may include: a detailed analysis of language design, semantics, verification, resource utilization, language support for concurrency, meta-programming, and compilers. May be taken more than once in different topics with permission of Department Chair.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 460','Networks and Communications ','An introduction to computer networks and communications. Topics include local and wide area networks, network architectures, security, communications protocols, routing, and an introduction to distributed computing.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 461','Embedded and Real-Time Software Systems ','The theory and practice of developing embedded systems with time and resource constraints. Students design, develop and deploy embedded systems on hardware ranging from bare-metal micro-controllers to systems with a real-time OS to Embedded Linux systems. Time-oriented topics include bare-metal programming, cooperative multitasking and preemptive multitasking.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 465','Advanced Topics in Software Engineering ','This course examines selected emerging and advanced topics in software engineering. Topics may include: software verification and validation techniques, techniques to model and analyze software processes, software design for various architectures (service-oriented, component-oriented, message-oriented), automation of software delivery pipelines, case studies of large scale software successes and failures. May be taken more than once in different topics with permission of Department Chair.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 469','Advanced Topics in Systems','This course covers selected emerging and advanced topics in Systems. Topics may include: system programming, distributed systems, peer-to-peer systems, clustered systems, distributed file systems, replicated systems, content distribution systems, fault-tolerant systems, multimedia systems, real-time systems, virtualized systems etc. May be taken more than once in different topics with permission of Department Chair.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 478','Advanced Topics in Data Science ','This course examines selected emerging and advanced topics in Data Science. Topics may include: big data, data visualization techniques, data mining, statistical modeling and prediction, emerging data analysis techniques. May be taken more than once in different topics with permission of Department Chair.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 479','Advanced Topics in Artificial Intelligence ','This course examines selected emerging and advanced topics in Artificial Intelligence. Topics may include: searching strategies, constraint satisfaction, game playing, knowledge representation and reasoning, machine learning, applications to robotics. May be taken more than once in different topics with permission of Department Chair. ', 0, 0,'All Sections',4,'Both'),
                ('CSCI 485','Advanced General Topics in Computer Science ','This course covers selected emerging and advanced topics in Computer Science. Topics may include: programming, systems, software engineering, human computer interaction, algorithms, artificial intelligence, data science, robotics. May be taken more than once in different topics with permission of Department Chair. ', 0, 0,'All Sections',4,'Both'),
                ('CSCI 485C','Topics in Systems: Advanced Algorithms ','Offered as CSCI 485A, 485B, 485C, 485D. Topics depend primarily on the interests of the instructor. Entry is restricted to third and fourth year students who meet the prerequisite specified for the topic to be offered. May be taken more than once in different topics with permission of department Chair. ', 0, 0,'All Sections',4,'Both'),
                ('CSCI 485F','Topics in Systems: Array Programming ','Topics depend primarily on the interests of the instructor. Entry is restricted to third and fourth year students who meet the prerequisite specified for the topic to be offered. May be taken more than once in different topics with permission of department Chair.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 490','Independent Project ','A one-semester independent research and development project under faculty supervision. Includes required research and development as per an approved project proposal, and preparation of a written report detailing the results.', 0, 0,'All Sections',4,'Both'),
                ('CSCI 491','Senior Research Project ','An opportunity for student experience in research and development under the supervision of a faculty member in Computing Science. Project duration is two academic terms during which time a student must develop an approved project proposal, carry out the required research and development, prepare a written report detailing results, and satisfy any additional requirements as specified in the approved project proposal.', 0, 0,'All Sections',4,'Both')
            ])

    # Student account dummy data
    password1 = '123'
    password2 = 'tacocat'
    password3 = 'ilikepasswords'
    password4 = 'iloveviu'
    password5 = 'csci375sucks'

    cursor.executemany("""
            INSERT INTO Students
            VALUES (?, ?, ?)
            """, [
                (1, 'Luka', hashlib.sha256(password1.encode()).hexdigest()),
                (2, 'Lachlan', hashlib.sha256(password2.encode()).hexdigest()),
                (3, 'Casey', hashlib.sha256(password3.encode()).hexdigest()),
                (4, 'alphasigmaTobin', hashlib.sha256(password4.encode()).hexdigest()),
                (5, 'Brandon', hashlib.sha256(password5.encode()).hexdigest())
            ])
    
    # Faculty member account dummy data
    password1 = '123'
    password2 = 'tacocat'
    password3 = 'ilikepasswords'
    password4 = 'iloveviu'
    password5 = 'csci375sucks'

    cursor.executemany("""
            INSERT INTO FacultyMembers
            VALUES (?, ?, ?)
            """, [
                (1, 'Luka', hashlib.sha256(password1.encode()).hexdigest()),
                (2, 'Lachlan', hashlib.sha256(password2.encode()).hexdigest()),
                (3, 'Casey', hashlib.sha256(password3.encode()).hexdigest()),
                (4, 'alphasigmaTobin', hashlib.sha256(password4.encode()).hexdigest()),
                (5, 'Brandon', hashlib.sha256(password5.encode()).hexdigest())
            ]) 

    # Review dummy data

    cursor.executemany("""INSERT INTO Reviews (reviewID, reviewText, difficulty, recommendedHours, reviewDate, courseID, studentID) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, [
        (1, 'The course was manageable, but I had to put in extra time to understand the concepts.', 3.2, 10, '2025-03-05', 'CSCI 112', 4),
        (2, 'Really enjoyed the hands-on approach. Assignments were challenging but fair.', 2.8, 8, '2025-02-28', 'CSCI 115', 2),
        (3, 'This course was intense but rewarding. Recommend brushing up on basics beforehand.', 4.5, 12, '2025-01-18', 'CSCI 159', 5),
        (4, 'Too fast-paced for a first-year course. Lectures were helpful though.', 3.7, 11, '2025-03-12', 'CSCI 160', 3),
        (5, 'Fantastic course for getting into programming. The prof made it fun.', 2.1, 6, '2025-02-01', 'CSCI 161', 1),
        (6, 'Found it hard to follow the textbook, but online resources helped.', 3.9, 9, '2025-01-30', 'CSCI 162', 2),
        (7, 'Loved the labs! Learned so much through practical assignments.', 2.6, 7, '2025-03-10', 'CSCI 251', 4),
        (8, 'Expect to spend long hours on this one. Not for the faint of heart.', 4.8, 14, '2025-01-15', 'CSCI 260', 5),
        (9, 'Interesting content but poorly organized. Midterm was brutal.', 3.4, 10, '2025-02-25', 'CSCI 261', 3),
        (10, 'A bit dry at times, but very useful skills were taught.', 2.5, 8, '2025-03-03', 'CSCI 265', 1),
        (11, 'Learned a lot about cyber-security. Real-world examples helped.', 3.0, 9, '2025-01-20', 'CSCI 301', 2),
        (12, 'Good prep for co-op. Got solid resume tips and mock interview practice.', 1.7, 4, '2025-02-22', 'CSCI 307', 3),
        (13, 'Great first work term experience. Felt supported by the coordinator.', 1.0, 3, '2025-01-27', 'CSCI 308', 4),
        (14, 'Second co-op was smoother. Got to work on real projects.', 1.2, 5, '2025-02-10', 'CSCI 309', 1),
        (15, 'HCI was fascinating! Loved the design challenges.', 2.4, 7, '2025-03-07', 'CSCI 310', 5),
        (16, 'Solid intro to web development. JavaScript portion was tricky.', 3.3, 9, '2025-01-14', 'CSCI 311', 2),
        (17, 'Theoretical but important. Automata were hard to grasp.', 4.0, 11, '2025-03-01', 'CSCI 320', 3),
        (18, 'Interesting to see how different languages work. Prolog blew my mind.', 2.9, 8, '2025-02-18', 'CSCI 330', 4),
        (19, 'OO design was abstract but the examples made it clearer.', 3.5, 10, '2025-01-22', 'CSCI 331', 1),
        (20, 'Logic circuits were a struggle. Lab time was super helpful.', 4.2, 13, '2025-03-15', 'CSCI 355', 5),
        (21, 'Operating systems was dense. Be ready to grind.', 4.7, 15, '2025-02-11', 'CSCI 360', 3),
        (22, 'Lots of database theory, but hands-on SQL was useful.', 3.1, 9, '2025-01-19', 'CSCI 370', 2),
        (23, 'Learned how to think like a systems analyst. Group project was cool.', 2.7, 6, '2025-03-09', 'CSCI 375', 4),
        (24, 'Great discussions on ethics in computing. Thought-provoking content.', 2.0, 5, '2025-02-04', 'CSCI 400', 1),
        (25, 'Graphics was awesome but math-heavy. OpenGL was tough to learn.', 4.3, 12, '2025-03-06', 'CSCI 405', 5),
        (26, 'Co-op three was the best yet. Worked on advanced tools.', 1.3, 4, '2025-01-31', 'CSCI 408', 3),
        (27, 'Capstone felt rushed. We needed more prep going in.', 4.1, 11, '2025-02-26', 'CSCI 409', 2),
        (28, 'Algorithms were fun to tackle. But expect long nights.', 4.6, 13, '2025-03-11', 'CSCI 422', 4),
        (29, 'Cool to explore experimental topics in class.', 3.6, 10, '2025-01-25', 'CSCI 429', 1),
        (30, 'Explored Rust in-depth. Would take again.', 2.2, 7, '2025-02-13', 'CSCI 439', 5),
        (31, 'Networking basics taught well. Diagrams were great.', 3.2, 8, '2025-03-14', 'CSCI 460', 2),
        (32, 'Loved the embedded system lab! Programming was intuitive.', 2.9, 7, '2025-01-16', 'CSCI 461', 3),
        (33, 'Challenging material, but very rewarding project work.', 4.4, 12, '2025-02-08', 'CSCI 465', 4),
        (34, 'Explored distributed systems—really opened my eyes.', 3.8, 9, '2025-03-02', 'CSCI 469', 1),
        (35, 'Loved the data science projects. Very hands-on.', 2.3, 6, '2025-01-21', 'CSCI 478', 5),
        (36, 'A bit too theoretical, but concepts were cool.', 3.0, 8, '2025-02-17', 'CSCI 479', 2),
        (37, 'Broad topic coverage, but lacked depth.', 2.6, 7, '2025-03-08', 'CSCI 485', 3),
        (38, 'Very technical—wouldn’t recommend unless you love math.', 4.9, 15, '2025-01-26', 'CSCI 485C', 4),
        (39, 'Array programming was surprisingly fun!', 1.9, 5, '2025-02-14', 'CSCI 485F', 1),
        (40, 'The independent project was the highlight of my degree.', 2.1, 6, '2025-03-13', 'CSCI 490', 5),
        (41, 'Needed more support for research design. Felt a bit lost.', 3.7, 10, '2025-02-19', 'CSCI 491', 2),
        (42, 'Enjoyed the freedom to explore my own ideas.', 2.0, 6, '2025-03-17', 'CSCI 490', 1),
        (43, 'Real sense of accomplishment after finishing the project.', 2.4, 8, '2025-02-03', 'CSCI 491', 3),
        (44, 'The course helped me understand complex systems more deeply.', 3.3, 9, '2025-01-23', 'CSCI 469', 4),
        (45, 'Great blend of theory and application.', 2.5, 7, '2025-02-06', 'CSCI 330', 5),
        (46, 'Learned more in this class than any other. Highly recommended.', 2.8, 8, '2025-03-04', 'CSCI 261', 2),
        (47, 'You’ll need strong math skills for this one.', 4.6, 14, '2025-01-28', 'CSCI 422', 3),
        (48, 'Wish there was more feedback on assignments.', 3.0, 9, '2025-02-15', 'CSCI 265', 1),
        (49, 'Tons of material to cover, but the prof was amazing.', 3.5, 10, '2025-03-16', 'CSCI 311', 4),
        (50, 'Straightforward course if you keep up weekly.', 2.0, 6, '2025-01-24', 'CSCI 115', 5),
        (51, 'Hard to stay motivated. Needed more interaction.', 3.4, 10, '2025-02-20', 'CSCI 160', 2),
        (52, 'Best course for understanding real-world computing issues.', 2.7, 7, '2025-03-18', 'CSCI 400', 3),
        (53, 'Group work was poorly organized.', 3.6, 9, '2025-02-12', 'CSCI 375', 1),
        (54, 'Felt underprepared for this level.', 4.0, 12, '2025-01-29', 'CSCI 355', 4),
        (55, 'Great TAs made a big difference.', 2.1, 6, '2025-03-05', 'CSCI 159', 5),
        (56, 'Labs were confusing and didn’t match lectures.', 3.9, 10, '2025-02-16', 'CSCI 162', 2),
        (57, 'One of the more innovative courses I’ve taken.', 2.3, 7, '2025-01-17', 'CSCI 439', 3),
        (58, 'Class discussions were the best part.', 2.5, 8, '2025-03-19', 'CSCI 307', 1),
        (59, 'Way too much theory for my liking.', 4.2, 11, '2025-02-21', 'CSCI 320', 4),
        (60, 'Practical course with real applications.', 2.2, 6, '2025-01-13', 'CSCI 370', 5),
        (61, 'Didn’t expect to enjoy this class but I did.', 2.0, 5, '2025-03-20', 'CSCI 112', 2),
        (62, 'The instructor was passionate and it showed.', 2.8, 7, '2025-02-07', 'CSCI 161', 3),
        (63, 'Learned more from the labs than the lectures.', 3.1, 9, '2025-03-21', 'CSCI 260', 4),
        (64, 'Enjoyed exploring new programming paradigms.', 3.0, 8, '2025-01-11', 'CSCI 330', 1),
        (65, 'Could use more structure. Felt chaotic at times.', 3.8, 10, '2025-02-02', 'CSCI 485', 5),
        (66, 'So many acronyms! It was overwhelming at first.', 3.9, 10, '2025-01-12', 'CSCI 251', 2),
        (67, 'Genuinely useful course. Took away a lot.', 2.4, 6, '2025-03-22', 'CSCI 311', 3),
        (68, 'Capstone was a rewarding challenge.', 3.2, 9, '2025-02-09', 'CSCI 490', 1),
        (69, 'Best experience of my degree.', 1.5, 4, '2025-01-10', 'CSCI 308', 4),
        (70, 'Not as useful as I hoped, but still okay.', 2.6, 7, '2025-03-23', 'CSCI 485F', 5)
    ])


    conn.commit()
    conn.close()

if __name__ == "__main__":
        insert()