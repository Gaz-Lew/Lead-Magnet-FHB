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

# Custom CSS for ASG branding
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@400;700&display=swap');
    
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #2D3748;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        color: #4A5568;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .asg-gold {
        background-color: #DAA520;
        color: #2D3748;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    .asg-navy {
        color: #2D3748;
    }
    
    .benefit-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #E2E8F0;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .benefit-card:hover {
        border-color: #DAA520;
        transition: border-color 0.2s;
    }
    
    .chapter-item {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
    }
    
    .chapter-number {
        background: #D2691E;
        color: white;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        margin-right: 1rem;
        font-size: 0.9rem;
    }
    
    .testimonial-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #E2E8F0;
        margin-bottom: 1rem;
    }
    
    .star-rating {
        color: #FFC107;
        font-size: 1.2rem;
    }
    
    .form-section {
        background: linear-gradient(135deg, #DAA520 0%, #F7DC6F 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }
    
    .success-message {
        background: #D4F8D4;
        border: 1px solid #68D391;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        color: #2F855A;
    }
    
    .footer-section {
        background: #2D3748;
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 3rem;
    }
    
    .asg-logo {
        background: #DAA520;
        color: #2D3748;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1.2rem;
        display: inline-block;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""

# Hero Section
st.markdown('<div class="asg-gold">🆓 FREE DOWNLOAD • 2025 EDITION</div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">Perth Property Playbook</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Step-by-Step Guide to Buying Smart in Western Australia</p>', unsafe_allow_html=True)

# Hero content box
with st.container():
    st.markdown("""
    <div style="background: rgba(255,255,255,0.9); padding: 2rem; border-radius: 15px; margin: 2rem 0; border: 2px solid #DAA520;">
        <p style="font-size: 1.2rem; color: #2D3748; margin-bottom: 1rem; text-align: center;">
            From first home to investment portfolio — discover the insider strategies that successful Perth property 
            buyers use to make informed decisions in today's market.
        </p>
        <div style="display: flex; justify-content: center; gap: 2rem; font-size: 0.9rem; color: #4A5568; flex-wrap: wrap;">
            <span>✓ Market Analysis & Trends</span>
            <span>✓ Suburb Selection Guide</span>
            <span>✓ Investment Strategies</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick jump to form button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎯 Get Your Free Guide Now", use_container_width=True, type="primary"):
        st.markdown('<script>document.getElementById("lead-form").scrollIntoView({behavior: "smooth"});</script>', unsafe_allow_html=True)

st.markdown("*No spam. Unsubscribe anytime. Trusted by 2,500+ Perth property buyers.*")

# Benefits Section
st.markdown("---")
st.markdown("## 🎯 What You'll Discover Inside")
st.markdown("*This comprehensive guide contains the strategies and insights that have helped thousands of buyers make smart property decisions in Perth.*")

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
            <div style="display: flex; align-items: start; gap: 1rem;">
                <div style="background: rgba(218, 165, 32, 0.2); padding: 1rem; border-radius: 10px; font-size: 1.5rem;">
                    {benefit["icon"]}
                </div>
                <div>
                    <h3 style="color: #2D3748; margin-bottom: 0.5rem; font-weight: 600;">{benefit["title"]}</h3>
                    <p style="color: #4A5568; margin: 0;">{benefit["description"]}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Guide Preview Section
st.markdown("---")
st.markdown("## 📚 Complete Table of Contents")
st.markdown("*8 comprehensive chapters covering everything you need to know about buying property in Perth*")

chapters = [
    "Chapter 1: Perth Market Overview & 2025 Trends",
    "Chapter 2: First Home Buyer's Complete Checklist", 
    "Chapter 3: The Suburb Selection Framework",
    "Chapter 4: Investment Property Strategies",
    "Chapter 5: Financing & Government Grants Guide",
    "Chapter 6: Negotiation Tactics That Work",
    "Chapter 7: Due Diligence & Inspection Checklist",
    "Chapter 8: Building Your Property Portfolio"
]

for i, chapter in enumerate(chapters, 1):
    st.markdown(f"""
    <div class="chapter-item">
        <div class="chapter-number">{i}</div>
        <span style="color: #2D3748; font-weight: 500;">{chapter}</span>
    </div>
    """, unsafe_allow_html=True)

# Bonus materials
st.markdown("""
<div style="background: #FFF8DC; padding: 1.5rem; border-radius: 10px; border: 2px solid #DAA520; margin-top: 1rem;">
    <h3 style="color: #2D3748; margin-bottom: 1rem;">🎁 Bonus Materials Included:</h3>
    <ul style="color: #4A5568;">
        <li>• Suburb comparison spreadsheet template</li>
        <li>• Property inspection checklist (printable PDF)</li>
        <li>• Mortgage broker contact list</li>
        <li>• Government grants eligibility calculator</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Social Proof Section
st.markdown("---")
st.markdown("## ⭐ Trusted by Perth Property Buyers")

col1, col2, col3 = st.columns(3)
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

for i, testimonial in enumerate(testimonials):
    with [col1, col2, col3][i]:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="star-rating">⭐⭐⭐⭐⭐</div>
            <p style="font-style: italic; color: #4A5568; margin: 1rem 0;">"{testimonial["text"]}"</p>
            <div style="font-weight: 600; color: #2D3748;">{testimonial["name"]}</div>
            <div style="color: #4A5568; font-size: 0.9rem;">{testimonial["location"]}</div>
        </div>
        """, unsafe_allow_html=True)

# Lead Capture Form Section
st.markdown("---")
st.markdown('<div id="lead-form"></div>', unsafe_allow_html=True)

if not st.session_state.form_submitted:
    st.markdown("""
    <div class="form-section">
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📧</div>
            <h2 style="color: #2D3748; margin-bottom: 1rem;">Get Your Free Guide Now</h2>
            <p style="color: #4A5568; font-size: 1.1rem;">Receive the complete Perth Property Playbook via email instantly</p>
            <p style="color: #4A5568; font-size: 0.9rem;">Join 2,500+ smart property buyers who've already received this guide</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("lead_capture_form"):
        st.markdown("**Are you currently renting or own a property?**")
        property_status = st.radio(
            "Property Status",
            ["Renting", "Own a property"], 
            label_visibility="collapsed"
        )
        
        st.markdown("**Are you ready to get into a home right now or just researching?**")
        readiness = st.radio(
            "Readiness",
            ["Ready to buy now", "Just researching"],
            label_visibility="collapsed"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("Full Name *", placeholder="Enter your full name")
        with col2:
            phone = st.text_input("Phone Number *", placeholder="Enter your phone number")
        
        email = st.text_input("Email Address (Optional)", placeholder="Enter your email address")
        
        submitted = st.form_submit_button("📧 Get Your Free Guide Now", use_container_width=True, type="primary")
        
        if submitted:
            if first_name and phone and property_status and readiness:
                st.session_state.form_submitted = True
                st.session_state.user_email = email if email else "your inbox"
                st.rerun()
            else:
                st.error("Please fill in all required fields (Name, Phone, Property Status, and Readiness)")

else:
    # Success message
    st.markdown(f"""
    <div class="success-message">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📧</div>
        <h2 style="color: #2F855A; margin-bottom: 1rem;">Check Your Email!</h2>
        <p style="font-size: 1.2rem; margin-bottom: 1rem;">
            Your Perth Property Playbook is being sent to <strong>{st.session_state.user_email}</strong>
        </p>
        <p style="color: #4A5568;">
            Don't forget to check your spam folder if you don't see it in the next few minutes.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("🔒 *Your information is 100% secure and will never be shared*")

# Footer
st.markdown("""
<div class="footer-section">
    <div class="asg-logo">ASG</div>
    <div style="color: #DAA520; font-size: 0.9rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 1px;">Amplify Solutions Group</div>
    <h3 style="color: #DAA520; font-family: 'Playfair Display', serif; font-size: 1.8rem; margin-bottom: 1rem;">Perth Property Playbook</h3>
    <p style="color: #A0AEC0; margin-bottom: 1.5rem;">Your trusted guide to smart property buying in Western Australia</p>
    <hr style="border-color: rgba(218, 165, 32, 0.2); margin: 1.5rem 0;">
    <p style="color: #A0AEC0; font-size: 0.9rem;">© 2025 Amplify Solutions Group. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
