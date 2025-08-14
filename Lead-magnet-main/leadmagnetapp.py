import streamlit as st
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Perth Property Playbook - Your Free Guide to Buying Smart in WA",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean white background with gold/navy theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;700&display=swap');
    
    /* Global styles */
    .main > div {
        padding-top: 2rem;
    }
    
    .stApp {
        background-color: white;
    }
    
    /* Fix font visibility for all Streamlit elements */
    .stSelectbox label, .stTextInput label, .stTextArea label, 
    .stRadio label, .stCheckbox label, .stMultiSelect label,
    .stNumberInput label, .stSlider label, .stDateInput label,
    .stTimeInput label, .stFileUploader label, .stColorPicker label,
    .stForm label, .stFormSubmitButton, .stButton > button,
    .stRadio > div, .stSelectbox > div, .stTextInput > div,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4,
    div[data-testid="stMarkdownContainer"] span {
        color: #000000 !important;
    }
    
    /* Ensure radio button text is visible */
    .stRadio > div > div > div > label {
        color: #000000 !important;
    }
    
    /* Form elements visibility */
    .stForm {
        color: #000000 !important;
    }
    
    /* Center all content */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
    }
    
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin: 1rem 0;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    .hero-badge {
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        color: #1e3a8a;
        padding: 0.75rem 1.5rem;
        border-radius: 30px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 2rem;
        text-align: center;
        font-size: 0.9rem;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.3);
    }
    
    .hero-content {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem auto;
        border: 3px solid #fbbf24;
        max-width: 800px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    }
    
    .hero-text {
        font-size: 1.2rem;
        color: #1e3a8a;
        margin-bottom: 1.5rem;
        font-weight: 500;
        line-height: 1.6;
    }
    
    .hero-features {
        display: flex;
        justify-content: center;
        gap: 2rem;
        font-size: 0.95rem;
        color: #1e3a8a;
        flex-wrap: wrap;
        font-weight: 600;
    }
    
    /* Section headers */
    .section-header {
        color: #1e3a8a;
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 3rem 0 1rem 0;
    }
    
    .section-subtitle {
        color: #1e3a8a;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* Benefits section - keep 4-box layout */
    .benefit-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #fbbf24;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(251, 191, 36, 0.1);
        transition: all 0.3s ease;
    }
    
    .benefit-card:hover {
        border-color: #1e3a8a;
        box-shadow: 0 8px 30px rgba(30, 58, 138, 0.15);
        transform: translateY(-2px);
    }
    
    .benefit-icon {
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        padding: 1rem;
        border-radius: 15px;
        font-size: 1.8rem;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
    }
    
    .benefit-title {
        color: #1e3a8a;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    
    .benefit-description {
        color: #374151;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Chapter items */
    .chapter-container {
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }
    
    .chapter-item {
        background: white;
        padding: 1.25rem;
        border-radius: 12px;
        border: 2px solid #fbbf24;
        margin: 0.75rem auto;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
        max-width: 700px;
        text-align: left;
    }
    
    .chapter-item:hover {
        border-color: #1e3a8a;
        box-shadow: 0 4px 15px rgba(30, 58, 138, 0.1);
    }
    
    .chapter-number {
        background: linear-gradient(135deg, #1e3a8a, #3730a3);
        color: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        margin-right: 1.5rem;
        font-size: 1rem;
        box-shadow: 0 3px 10px rgba(30, 58, 138, 0.3);
    }
    
    .chapter-text {
        color: #1e3a8a;
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* Bonus materials */
    .bonus-section {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #fbbf24;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 4px 20px rgba(251, 191, 36, 0.1);
    }
    
    .bonus-title {
        color: #1e3a8a;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .bonus-list {
        color: #1e3a8a;
        font-weight: 500;
        list-style: none;
        padding-left: 0;
        text-align: center;
    }
    
    .bonus-list li {
        margin-bottom: 0.5rem;
        padding-left: 1.5rem;
        position: relative;
    }
    
    .bonus-list li:before {
        content: "✨";
        position: absolute;
        left: 0;
    }
    
    /* Testimonials */
    .testimonial-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #fbbf24;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(251, 191, 36, 0.1);
        text-align: center;
    }
    
    .star-rating {
        color: #fbbf24;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }
    
    .testimonial-text {
        font-style: italic;
        color: #374151;
        margin: 1rem 0;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    .testimonial-name {
        font-weight: 700;
        color: #1e3a8a;
        font-size: 1rem;
    }
    
    .testimonial-location {
        color: #6b7280;
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }
    
    /* Form section */
    .form-container {
        max-width: 600px;
        margin: 3rem auto;
        background: white;
        padding: 3rem;
        border-radius: 20px;
        border: 3px solid #fbbf24;
        box-shadow: 0 8px 30px rgba(251, 191, 36, 0.2);
    }
    
    .form-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .form-title {
        color: #1e3a8a;
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .form-subtitle {
        color: #1e3a8a;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .form-description {
        color: #6b7280;
        font-size: 0.9rem;
        font-style: italic;
    }
    
    /* Success message */
    .success-container {
        max-width: 600px;
        margin: 3rem auto;
        background: linear-gradient(135deg, #d1fae5, #a7f3d0);
        border: 3px solid #10b981;
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        box-shadow: 0 8px 30px rgba(16, 185, 129, 0.2);
    }
    
    .success-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .success-title {
        color: #047857;
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .success-text {
        color: #047857;
        font-size: 1.2rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    .success-note {
        color: #374151;
        font-size: 0.95rem;
    }
    
    /* Footer */
    .footer-section {
        background: linear-gradient(135deg, #1e3a8a, #3730a3);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 4rem auto 2rem auto;
        max-width: 800px;
        box-shadow: 0 8px 30px rgba(30, 58, 138, 0.3);
    }
    
    .asg-logo {
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        color: #1e3a8a;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.3rem;
        display: inline-block;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.3);
    }
    
    .footer-brand {
        color: #fbbf24;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    .footer-title {
        color: #fbbf24;
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .footer-subtitle {
        color: #e5e7eb;
        margin-bottom: 1.5rem;
        font-size: 1rem;
    }
    
    .footer-copyright {
        color: #9ca3af;
        font-size: 0.9rem;
        border-top: 1px solid rgba(251, 191, 36, 0.2);
        padding-top: 1.5rem;
        margin-top: 1.5rem;
    }
    
    /* Center content wrapper */
    .centered-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""

# Hero Section
st.markdown('<div class="centered-content">', unsafe_allow_html=True)

# Hero badge
st.markdown('<div style="text-align: center;"><span class="hero-badge">🆓 FREE DOWNLOAD • 2025 EDITION</span></div>', unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">Perth Property Playbook</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Step-by-Step Guide to Buying Smart in Western Australia</p>', unsafe_allow_html=True)

# Hero content box
st.markdown("""
<div class="hero-content">
    <p class="hero-text">
        From first home to investment portfolio — discover the insider strategies that successful Perth property 
        buyers use to make informed decisions in today's market.
    </p>
    <div class="hero-features">
        <span>✓ Market Analysis & Trends</span>
        <span>✓ Suburb Selection Guide</span>
        <span>✓ Investment Strategies</span>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎯 Get Your Free Guide Now", use_container_width=True, type="primary"):
        pass

st.markdown("<div style='text-align: center; margin: 1.5rem 0; color: #6b7280; font-style: italic;'>No spam. Unsubscribe anytime. Trusted by 2,500+ Perth property buyers.</div>", unsafe_allow_html=True)

# Benefits Section
st.markdown('<h2 class="section-header">What You\'ll Discover Inside</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">This comprehensive guide contains the strategies and insights that have helped thousands of buyers make smart property decisions in Perth.</p>', unsafe_allow_html=True)

benefits = [
    {
        "icon": "🏠",
        "title": "First Home Buyer Secrets",
        "description": "Navigate grants, loans, and hidden costs with confidence. Avoid the common mistakes that cost buyers thousands."
    },
    {
        "icon": "📈",
        "title": "Investment Strategies", 
        "description": "Learn which Perth suburbs offer the best growth potential and rental yields for building long-term wealth."
    },
    {
        "icon": "📍",
        "title": "Suburb Selection Matrix",
        "description": "Our exclusive scoring system helps you identify undervalued areas before they boom."
    },
    {
        "icon": "🧮",
        "title": "Financial Planning Tools",
        "description": "Calculate borrowing capacity, stamp duty, and ongoing costs with our proven formulas."
    }
]

col1, col2 = st.columns(2)
for i, benefit in enumerate(benefits):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="benefit-card">
            <div class="benefit-icon">{benefit["icon"]}</div>
            <div class="benefit-title">{benefit["title"]}</div>
            <div class="benefit-description">{benefit["description"]}</div>
        </div>
        """, unsafe_allow_html=True)

# Guide Preview Section
st.markdown('<h2 class="section-header">Complete Table of Contents</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">8 comprehensive chapters covering everything you need to know about buying property in Perth</p>', unsafe_allow_html=True)

chapters = [
    "Chapter 1: Perth Market Overview & 2025 Trends",
    "Chapter 2: First Home Buyer's Complete Checklist", 
    "Chapter 3: The Suburb Selection Framework",
    "Chapter 4: Investment Property Strategies",
    "Chapter 5: Brokerage Advice for First Home Buyers & Government Grants Guide",
    "Chapter 6: Negotiation Tactics That Work",
    "Chapter 7: Due Diligence & Inspection Checklist",
    "Chapter 8: Building Your Property Portfolio"
]

st.markdown('<div class="chapter-container">', unsafe_allow_html=True)
for i, chapter in enumerate(chapters, 1):
    st.markdown(f"""
    <div class="chapter-item">
        <div class="chapter-number">{i}</div>
        <span class="chapter-text">{chapter}</span>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Bonus materials
st.markdown("""
<div class="bonus-section">
    <div class="bonus-title">🎁 Bonus Materials Included:</div>
    <ul class="bonus-list">
        <li>Suburb comparison spreadsheet template</li>
        <li>Property inspection checklist (printable PDF)</li>
        <li>Mortgage broker contact list</li>
        <li>Government grants eligibility calculator</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Social Proof Section
st.markdown('<h2 class="section-header">Trusted by Perth Property Buyers</h2>', unsafe_allow_html=True)
st.markdown("<div style='text-align: center; margin-bottom: 2rem;'><span style='color: #fbbf24; font-size: 2rem;'>⭐⭐⭐⭐⭐</span><br><strong style='color: #1e3a8a; font-size: 1.2rem;'>4.9/5 from 2,500+ downloads</strong></div>", unsafe_allow_html=True)

testimonials = [
    {
        "name": "Sarah M.",
        "location": "Joondalup", 
        "text": "This guide helped me find my first home in the perfect suburb. The suburb selection matrix was a game-changer!",
        "rating": 5
    },
    {
        "name": "David L.",
        "location": "Fremantle",
        "text": "As an investor, the strategies in this guide helped me identify undervalued properties before they took off.",
        "rating": 5
    },
    {
        "name": "Emma K.",
        "location": "Subiaco", 
        "text": "Saved me thousands on my purchase. The negotiation tactics actually work in the Perth market.",
        "rating": 5
    }
]

col1, col2, col3 = st.columns(3)
for i, testimonial in enumerate(testimonials):
    with [col1, col2, col3][i]:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="star-rating">⭐⭐⭐⭐⭐</div>
            <div class="testimonial-text">"{testimonial["text"]}"</div>
            <div class="testimonial-name">{testimonial["name"]}</div>
            <div class="testimonial-location">{testimonial["location"]}</div>
        </div>
        """, unsafe_allow_html=True)

# Lead Capture Form Section
if not st.session_state.form_submitted:
    st.markdown("""
    <div class="form-container">
        <div class="form-header">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📧</div>
            <div class="form-title">Get Your Free Guide Now</div>
            <div class="form-subtitle">Receive the complete Perth Property Playbook via email instantly</div>
            <div class="form-description">Join 2,500+ smart property buyers who've already received this guide</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create form in a container
    with st.container():
        with st.form("lead_capture_form"):
            # Questions in 2x2 grid
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Are you currently renting or own a property?")
                property_status = st.radio(
                    "Property Status",
                    ["Renting", "Own a property"], 
                    label_visibility="collapsed"
                )
                
                st.markdown("#### Have you been pre-approved for a loan?")
                pre_approved = st.radio(
                    "Pre-approved",
                    ["Yes", "No"],
                    label_visibility="collapsed"
                )
            
            with col2:
                st.markdown("#### Are you ready to get into a home right now or just researching?")
                readiness = st.radio(
                    "Readiness",
                    ["Ready to buy now", "Just researching"],
                    label_visibility="collapsed"
                )
                
                st.markdown("#### Would you like a free financial health check with one of our finance experts?")
                health_check = st.radio(
                    "Health Check",
                    ["Yes", "No"],
                    label_visibility="collapsed"
                )
            
            st.markdown("---")
            st.markdown("#### Contact Information")
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("Full Name *", placeholder="Enter your full name")
            with col2:
                phone = st.text_input("Phone Number *", placeholder="Enter your phone number")
            
            email = st.text_input("Email Address *", placeholder="Enter your email address")
            
            submitted = st.form_submit_button("📧 Get Your Free Guide Now", use_container_width=True, type="primary")
            
            if submitted:
                if first_name and phone and email and property_status and readiness and pre_approved and health_check:
                    st.session_state.form_submitted = True
                    st.session_state.user_email = email
                    st.rerun()
                else:
                    st.error("Please fill in all required fields")

else:
    # Success message
    st.markdown(f"""
    <div class="success-container">
        <div class="success-icon">📧</div>
        <div class="success-title">Check Your Email!</div>
        <div class="success-text">
            Your Perth Property Playbook has been sent to <strong>{st.session_state.user_email}</strong>
        </div>
        <div class="success-note">
            Don't forget to check your spam folder if you don't see it in the next few minutes.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='text-align: center; margin: 2rem 0; color: #6b7280; font-style: italic;'>🔒 Your information is 100% secure and will never be shared</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer-section">
    <div class="asg-logo">ASG</div>
    <div class="footer-brand">Amplify Solutions Group</div>
    <div class="footer-title">Perth Property Playbook</div>
    <div class="footer-subtitle">Your trusted guide to smart property buying in Western Australia</div>
    <div class="footer-copyright">© 2025 Amplify Solutions Group. All rights reserved.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
