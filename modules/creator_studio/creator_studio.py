import streamlit as st

def show_creator_studio(creators=None):
    st.header("✨ AI Showcase & Creator Studio")
    
    tabs = st.tabs(["🎨 AI Showcase", "📋 Brand Briefs", "🔍 Creator Search & Filtering"])
    
    # ------------------- TAB 1: AI SHOWCASE -------------------
    with tabs[0]:
        st.subheader("Showcase AI-Generated Work")
        st.caption("Publish your videos, animations, and graphics with full tool lineage & verification.")
        
        with st.form("showcase_form"):
            col1, col2 = st.columns(2)
            with col1:
                title = st.text_input("Work Title", "Cinematic Cyberpunk Short")
                content_type = st.selectbox("Content Type", ["Video", "Animation", "Graphics", "3D Asset"])
                models = st.multiselect(
                    "Tools / Models Used", 
                    ["Midjourney v6", "Runway Gen-2", "Stable Diffusion XL", "OpenAI DALL-E 3", "Pika Labs", "ComfyUI"],
                    default=["Midjourney v6", "Runway Gen-2"]
                )
            with col2:
                specialization = st.text_input("Specialization", "Photorealistic Sci-Fi Concept Art")
                skills = st.text_input("Skills (comma-separated)", "Prompt Engineering, ControlNet, Motion Graphics, Inpainting")
                aspect_ratio = st.selectbox("Aspect Ratio", ["16:9", "9:16", "1:1", "4:5"])

            workflow_info = st.text_area(
                "Relevant Workflow Information", 
                "Generated keyframes in Midjourney v6 -> Upscaled via Topaz -> Animated camera motion using Runway Gen-2."
            )
            
            is_verified = st.checkbox("🔒 Enable Verification Signal (Attach Verified Credentials)", value=True)
            
            submit_work = st.form_submit_button("🚀 Publish to Showcase")
            if submit_work:
                st.success("Work published successfully with verified tool metadata!")
                if is_verified:
                    st.info("✅ Verified Creator Signal Active")

    # ------------------- TAB 2: BRAND / AGENCY BRIEFS -------------------
    with tabs[1]:
        st.subheader("Define Brand & Agency Briefs")
        
        with st.form("brand_brief_form"):
            brief_title = st.text_input("Campaign Title", "Summer Product Launch 2026")
            col_a, col_b = st.columns(2)
            with col_a:
                req_type = st.selectbox("Content Type Required", ["Video", "Animation", "Graphics", "Mixed Media"])
                req_format = st.selectbox("Format / Aspect Ratio", ["9:16 (Vertical / Reels)", "16:9 (Horizontal)", "1:1 (Square)"])
            with col_b:
                req_style = st.text_input("Style / Aesthetic", "Vibrant, Minimalist, Cyberpunk")
                commercial_use = st.checkbox("Requires Full Commercial-Use License", value=True)
                
            brief_reqs = st.text_area("Campaign Requirements", "Need 3 short video spots highlighting sustainability features.")
            
            submit_brief = st.form_submit_button("📢 Publish Brief")
            if submit_brief:
                st.success("Brand brief published successfully!")

    # ------------------- TAB 3: SEARCH & FILTERING -------------------
    with tabs[2]:
        st.subheader("Filter Creators by Skill, Model & Verification")
        
        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            filter_skill = st.text_input("Search Skill", "ControlNet")
        with col_f2:
            filter_tool = st.selectbox("Tool / Model", ["All", "Midjourney v6", "Runway Gen-2", "Stable Diffusion XL"])
        with col_f3:
            only_verified = st.checkbox("Only Verified Creators", value=True)
            
        st.markdown("---")
        
        # Safely parse whatever format 'creators' is given in
        parsed_creators = []
        if isinstance(creators, list):
            for item in creators:
                if isinstance(item, dict):
                    parsed_creators.append(item)
                elif isinstance(item, str):
                    parsed_creators.append({
                        "name": item, 
                        "specialization": "General AI Creator", 
                        "tools": ["Various"], 
                        "skills": [item], 
                        "verified": True, 
                        "badge": "🛡️ Verified"
                    })
        
        # Fallback to sample data if list is empty or invalid
        if not parsed_creators:
            parsed_creators = [
                {
                    "name": "Elena Rostova",
                    "specialization": "3D Product Animation",
                    "tools": ["Midjourney v6", "Runway Gen-2"],
                    "skills": ["ControlNet", "Lighting", "Color Grading"],
                    "verified": True,
                    "badge": "🛡️ Verified Tools & Workflow"
                },
                {
                    "name": "Marcus Vance",
                    "specialization": "AI Concept Design",
                    "tools": ["Stable Diffusion XL", "ComfyUI"],
                    "skills": ["Inpainting", "Prompt Engineering"],
                    "verified": True,
                    "badge": "🛡️ Verified Credentials"
                }
            ]
        
        for c in parsed_creators:
            if not only_verified or c.get("verified", True):
                with st.expander(f"{c.get('name', 'Creator')} — {c.get('specialization', 'AI Creator')}"):
                    if c.get("verified", True):
                        st.markdown(f"**Verification:** `{c.get('badge', 'Verified')}`")
                    
                    tools_val = c.get('tools', [])
                    tools_str = ', '.join(tools_val) if isinstance(tools_val, list) else str(tools_val)
                    st.write(f"**Tools:** {tools_str}")
                    
                    skills_val = c.get('skills', [])
                    skills_str = ', '.join(skills_val) if isinstance(skills_val, list) else str(skills_val)
                    st.write(f"**Skills:** {skills_str}")