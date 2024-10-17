# Let's retry loading the images into the PDF with new paths
from fpdf import FPDF

pdf = FPDF()

# Add a title page
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, txt="Kids Fun Yoga Poses", ln=True, align="C")
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Here are some fun and simple yoga poses with playful names designed for kids. "
    "These stretches will help children engage and enjoy the practice while staying active!",
)
pdf.image("joga_pose_images/Kids_Fun_Yoga_Poses.png", x=20, y=60, w=170, h=170)


# Add images and instructions for each pose

# Pose 1: Reach for the Stars (Mountain Pose)
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="1. Reach for the Stars Pose (Mountain Pose)", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Stand tall with feet together, arms at your sides. Slowly raise your arms up to the sky "
    "like you're trying to touch the stars. Reach as high as you can!",
)
pdf.image("joga_pose_images/Reach_for_the_Stars_Pose.png", x=30, y=60, w=150, h=150)

# Pose 2: Cat and Cow
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="2. Cat and Cow Pose", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Start on your hands and knees. Arch your back up like a cat, then let your belly drop and "
    "look up like a cow. Keep alternating between cat and cow slowly.",
)
pdf.image("joga_pose_images/Cat_and_Cow_Pose.png", x=30, y=60, w=150, h=150)

# Pose 3: Airplane Pose (Warrior III)
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="3. Airplane Pose (Warrior III)", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Stand tall, then lean forward with one leg stretched out behind you and your arms spread "
    "wide like airplane wings. Try balancing and soaring like a plane!",
)
pdf.image("joga_pose_images/Airplane_Pose.png", x=30, y=60, w=150, h=150)

# Pose 4: Butterfly Wings Pose (Butterfly Pose)
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="4. Butterfly Wings Pose (Butterfly Pose)", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Sit on the floor, bring the soles of your feet together, and gently flap your knees up and "
    "down like butterfly wings. You can also pretend you're flying!",
)
pdf.image("joga_pose_images/Butterfly_Wings_Pose.png", x=30, y=60, w=150, h=150)

# Pose 5: Cobra Pose
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="5. Cobra Pose", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Lie on your belly with your hands under your shoulders. Push up with your hands, lifting "
    "your chest while keeping your hips on the ground. Imagine you are a snake slithering through the grass!",
)
pdf.image("joga_pose_images/Cobra_Pose.png", x=30, y=60, w=150, h=150)

# Pose 6: Tree Pose
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="6. Tree Pose", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Stand tall and slowly lift one foot, placing it on your other leg. Hold your arms above your "
    "head like branches. Try balancing and being a still, strong tree!",
)
pdf.image("joga_pose_images/Tree_Pose.png", x=30, y=60, w=150, h=150)

# Pose 7: Downward Dog Pose
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, txt="7. Downward Dog Pose", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(
    0,
    10,
    txt="Start on your hands and knees, then lift your hips up to the sky to make a triangle shape. "
    "Walk your feet back if needed and wag your 'tail' like a dog!",
)
pdf.image("joga_pose_images/Downward_Dog_Pose.png", x=30, y=60, w=150, h=150)

# Save the PDF to a file
output_path = "Kids_Yoga_Poses_Final.pdf"
pdf.output(output_path)

output_path
