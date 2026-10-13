import streamlit as st
<<<<<<< HEAD
import pandas as pd
from modules.creator_studio.creator_studio import show_creator_studio
=======
from modules.ai_matching.matcher import Brief, rank_creators
from modules.ai_matching.db import fetch_creators
from modules.ai_matching.filters import filter_creator_dicts, get_filter_options_from_dicts
>>>>>>> 5aa98fa6457ce71ab5be69527e98187722990b0a

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Prismatch",
    page_icon="✨",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", ["Dashboard", "Creator Studio", "Smart Brief Builder"])

# ---------------------------------------------------------
# APPLICATION HEADER
# ---------------------------------------------------------
st.title("✨ Prismatch")
st.subheader("AI-Native Creator Marketplace")

st.write(
    "Helping brands discover creators who match their campaign goals, "
    "creative style, and budget."
)

st.markdown("---")

# ---------------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------------
if page == "Dashboard":
    st.header("📊 Marketplace Dashboard")
    st.write("Welcome to Prismatch! Use the navigation sidebar to explore the Creator Studio or Smart Brief Builder.")
    
elif page == "Creator Studio":
    # Safely call creator studio
    show_creator_studio()

<<<<<<< HEAD
elif page == "Smart Brief Builder":
    st.header("📋 Smart Brand Brief Builder")
    st.write("Create and broadcast campaign briefs to verified AI creators.")
    with st.form("brief_builder_form"):
        st.text_input("Campaign Name", "AI Commercial Video Launch")
        st.selectbox("Content Type", ["Video", "Animation", "Graphics"])
        st.form_submit_button("Submit Brief")
=======
# 5. Top Icon Navigation Header
header_left, header_right = st.columns([1, 4])
with header_left:
    st.markdown("<div style='padding-top:4px;'><span class='brand-title'>✨ CreoVate_Ai</span></div>", unsafe_allow_html=True)

with header_right:
    nav_cols = st.columns([1.1, 1.3, 1.2, 1.4, 1.3, 1.2, 1.8])
    with nav_cols[0]:
        if st.button("🔑 Login", use_container_width=True, type="primary" if st.session_state["page"] == "Login / Sign Up" else "secondary"):
            st.session_state["page"] = "Login / Sign Up"
            rerun_app()
    with nav_cols[1]:
        if st.button("📊 Dashboard", use_container_width=True, type="primary" if st.session_state["page"] == "Dashboard" else "secondary"):
            st.session_state["page"] = "Dashboard"
            rerun_app()
    with nav_cols[2]:
        if st.button("👥 Studio", use_container_width=True, type="primary" if st.session_state["page"] == "Creator Studio" else "secondary"):
            st.session_state["page"] = "Creator Studio"
            rerun_app()
    with nav_cols[3]:
        if st.button("⚡ Brief AI", use_container_width=True, type="primary" if st.session_state["page"] == "Smart Brief Builder" else "secondary"):
            st.session_state["page"] = "Smart Brief Builder"
            rerun_app()
    with nav_cols[4]:
        if st.button("🎯 Matching", use_container_width=True, type="primary" if st.session_state["page"] == "Matching Results" else "secondary"):
            st.session_state["page"] = "Matching Results"
            rerun_app()
    with nav_cols[5]:
        if st.button("👤 Profile", use_container_width=True, type="primary" if st.session_state["page"] == "Creator Profile" else "secondary"):
            st.session_state["page"] = "Creator Profile"
            rerun_app()
    with nav_cols[6]:
        st.markdown("<div style='text-align:right;padding-top:6px;'><span style='color:#10b981;'>●</span> <b>Brand User</b> <span style='color:#94a3b8;font-size:11px;'>@Acme</span></div>", unsafe_allow_html=True)

st.markdown("<hr style='margin:8px 0 24px 0; border:none; border-bottom:1px solid #e2e8f0;'/>", unsafe_allow_html=True)


# ==========================================
# 1. LOGIN / SIGN UP
# ==========================================
if st.session_state["page"] == "Login / Sign Up":
    l1, l2 = st.columns([1, 1], gap="large")
    with l1:
        st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
        st.markdown("<span style='color:#047857;font-size:12px;font-weight:700;letter-spacing:1px;'>AI-POWERED CREATOR PLATFORM</span>", unsafe_allow_html=True)
        st.markdown("<h1 style='color:#0f172a;font-size:32px;margin:8px 0 16px 0;line-height:1.2;'>Connect with creators that move numbers.</h1>", unsafe_allow_html=True)
        st.write("Match campaigns with creators using performance indicators, audience overlap, and verified engagement rates.")
        st.markdown("- ⚡ **Smart Compatibility Engine**: Multi-factor scoring\n- 🛡️ **Verified Creator Metrics**: Real-time engagement and view benchmarks\n- ⏱️ **Fast Turnarounds**: Move from brief formulation to outreach in minutes")
        st.markdown("</div>", unsafe_allow_html=True)
    with l2:
        st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
        st.subheader("Welcome Back")
        st.caption("Sign in to your CreoVate_Ai workspace")
        with st.form("login_form"):
            st.text_input("Work Email", value="you@brand.com")
            st.text_input("Password", type="password", value="••••••••••••")
            st.checkbox("Keep me signed in", value=True)
            if st.form_submit_button("Sign In →", use_container_width=True):
                st.session_state["page"] = "Dashboard"
                rerun_app()
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 2. DASHBOARD
# ==========================================
elif st.session_state["page"] == "Dashboard":
    st.subheader("Campaign Command Center")
    st.caption("Monitor brand operations, creator recommendations, and live spend metrics.")

    # 4-Column Metric Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Active Campaigns</div><div class="kpi-val">{len(st.session_state["campaigns"])}</div><div class="kpi-delta">↑ +1 added this week</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Verified Creators</div><div class="kpi-val">{len(st.session_state["creators"])}</div><div class="kpi-delta">↑ +5 added to network</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Collaborations</div><div class="kpi-val">2</div><div class="kpi-delta">↑ Active pipeline</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="kpi-card"><div class="kpi-title">Total Spend</div><div class="kpi-val">$2,400</div><div class="kpi-delta">↑ 14% budget remaining</div></div>', unsafe_allow_html=True)

    st.write("")
    c_left, c_right = st.columns([2, 1], gap="medium")

    with c_left:
        st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
        st.markdown("<b style='font-size:15px;color:#0f172a;'>Recent Campaigns</b>", unsafe_allow_html=True)
        st.write("")
        for cmp in st.session_state["campaigns"]:
            r1, r2, r3, r4 = st.columns([3, 1, 1, 1])
            r1.markdown(f"**{cmp['name']}**  \n<span style='font-size:11px;color:#64748b;'>{cmp['niche']}</span>", unsafe_allow_html=True)
            r2.markdown(f"<span class='match-pill'>{cmp['status']}</span>", unsafe_allow_html=True)
            r3.markdown(f"<b>{cmp['budget']}</b>", unsafe_allow_html=True)
            r4.caption(cmp["created"])
            st.markdown("<hr style='margin:8px 0; border:none; border-bottom:1px solid #f1f5f9;'/>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c_right:
        st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
        st.markdown("<b style='font-size:15px;color:#0f172a;'>Top Performing Creators</b>", unsafe_allow_html=True)
        st.write("")
        for c in st.session_state["creators"][:3]:
            tc1, tc2 = st.columns([1, 3])
            tc1.image(c["avatar"], width=46)
            tc2.markdown(f"**{c['name']}**  \n<span style='font-size:11px;color:#64748b;'>{c['followers']} • {c['engagement']} ER</span>", unsafe_allow_html=True)
            st.markdown("<hr style='margin:8px 0; border:none; border-bottom:1px solid #f1f5f9;'/>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 3. CREATOR STUDIO
# ==========================================
elif st.session_state["page"] == "Creator Studio":
    s_top1, s_top2 = st.columns([3, 1])
    with s_top1:
        st.subheader("Creator Discovery Directory")
        st.caption("Browse curated creator profiles, filter by performance metrics, and review portfolios.")
    with s_top2:
        if st.button("+ Create Campaign Brief", type="primary", use_container_width=True):
            st.session_state["page"] = "Smart Brief Builder"
            rerun_app()

    options = get_filter_options_from_dicts(st.session_state["creators"])

    f1, f2, f3 = st.columns([2, 1, 1])
    q_search = f1.text_input("Search", placeholder="Search name, skill, tool or niche...", label_visibility="collapsed")
    f_niche = f2.multiselect("Niche", options["niches"], placeholder="Niche", label_visibility="collapsed")
    f_type = f3.multiselect("Content type", options["content_types"], placeholder="Content type", label_visibility="collapsed")

    g1, g2, g3, g4 = st.columns([1, 1, 1, 1])
    f_tools = g1.multiselect("Tools", options["tools"], placeholder="Tools", label_visibility="collapsed")
    f_skills = g2.multiselect("Skills", options["skills"], placeholder="Skills", label_visibility="collapsed")
    f_budget = g3.slider("Max budget ($, 0 = any)", 0, 2000, 0, step=50)
    with g4:
        verified_only = st.checkbox("✅ Verified only")
        show_shortlist = st.checkbox("⭐ Show Shortlisted")

    filtered = filter_creator_dicts(
        st.session_state["creators"],
        niches=f_niche, content_types=f_type, tools=f_tools, skills=f_skills,
        max_budget=f_budget, verified_only=verified_only, query=q_search,
    )
    if show_shortlist:
        filtered = [c for c in filtered if c["id"] in st.session_state["shortlist"]]
    if not filtered:
        st.info("No creators match these filters. Try removing one filter.")

    grid_cols = st.columns(3)
    for idx, c in enumerate(filtered):
        with grid_cols[idx % 3]:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            st.image(c["avatar"], width=62)
            st.markdown(f"**{c['name']} ✓**")
            st.caption(f"{c['handle']} · 👥 {c['followers']} · 📈 {c['engagement']}")
            st.markdown(" ".join([f"<span class='tag-pill'>{n}</span>" for n in (c.get("niches") or [])]), unsafe_allow_html=True)
            st.write("")
            b_fav, b_view = st.columns(2)
            is_faved = c["id"] in st.session_state["shortlist"]
            if b_fav.button("❤️ Shortlisted" if is_faved else "🤍 Shortlist", key=f"fav_{c['id']}", use_container_width=True):
                if is_faved:
                    st.session_state["shortlist"].remove(c["id"])
                else:
                    st.session_state["shortlist"].add(c["id"])
                rerun_app()

            if b_view.button("View Profile", key=f"view_cs_{c['id']}", use_container_width=True):
                st.session_state["selected"] = c
                st.session_state["page"] = "Creator Profile"
                rerun_app()
            st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 4. SMART BRIEF BUILDER
# ==========================================
elif st.session_state["page"] == "Smart Brief Builder":
    st.subheader("Smart Campaign Brief Wizard")
    st.caption("Provide campaign requirements to calculate instant match scores across creators.")

    f_col, s_col = st.columns([2, 1], gap="large")
    with f_col:
        st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
        with st.form("brief_form"):
            c_name = st.text_input("Campaign Name *", value="Summer Glow Skincare Launch")
            c_brand = st.text_input("Brand / Company *", value="Acme Cosmetics")

            b1, b2 = st.columns(2)
            c_goal = b1.selectbox("Campaign Goal *", ["Brand Awareness", "Conversions", "UGC Production"])
            c_product = b2.text_input("Product / Service *", value="Organic Vitamin C Serum")

            selected_niches = st.multiselect(
                "Target Creator Niches *",
                ["Fashion", "Beauty", "Lifestyle", "Tech", "Fitness", "Food", "Travel", "Comedy"],
                default=["Beauty", "Lifestyle"]
            )

            b3, b4 = st.columns(2)
            c_format = b3.selectbox("Format", ["Short-form Video", "Carousel", "Tutorials", "Long-form Video"])
            c_budget = b4.slider("Budget per Creator ($)", 300, 2000, 800, step=50)

            c_desc = st.text_area("Creative Guidelines *", value="Focus on natural application, texture close-ups, and genuine unboxing reactions.")

            b5, b6 = st.columns(2)
            c_aspect = b5.selectbox("Aspect Ratio", ["Any", "9:16", "1:1", "4:5", "16:9"])
            c_commercial = b6.checkbox("Commercial use required", value=True)

            if st.form_submit_button("⚡ Run AI Matching Engine →", use_container_width=True):
                brief = Brief(
                    title=c_name,
                    goal=f"{c_goal} {c_product}",
                    audience=c_brand,
                    content_type=c_format,
                    niches=selected_niches,
                    style=c_desc,
                    budget=c_budget,
                    aspect_ratio="" if c_aspect == "Any" else c_aspect,
                    commercial_use=c_commercial,
                    currency="$",
                )
                recalculated = rank_creators(st.session_state["creators"], brief)
                st.session_state["matches"] = recalculated
                st.session_state["campaigns"].insert(0, {
                    "name": c_name,
                    "niche": f"{selected_niches[0] if selected_niches else 'General'} • Live",
                    "status": "Active",
                    "creators": len(recalculated),
                    "budget": f"${c_budget}",
                    "created": "Today"
                })
                st.session_state["page"] = "Matching Results"
                rerun_app()
        st.markdown("</div>", unsafe_allow_html=True)

    with s_col:
        st.markdown("<div class='saas-card' style='background:#f0fdf4;border-color:#bbf7d0;'>", unsafe_allow_html=True)
        st.markdown("<b style='color:#047857;font-size:13px;'>Algorithmic Scoring Model</b>", unsafe_allow_html=True)
        st.write("")
        st.markdown("- 🎯 **Niche Fit (30%)**\n- 📹 **Content Type (25%)**\n- 🔎 **Brief Keywords (15%)**\n- 💰 **Budget Alignment (15%)**\n- 📐 **Aspect Ratio (10%)**\n- 🛡️ **Trust Signals (5%)**")
        st.write("")
        st.info("The match model recalibrates dynamically as soon as you submit the form.")
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 5. MATCHING RESULTS
# ==========================================
elif st.session_state["page"] == "Matching Results":
    st.subheader("Ranked Creator Recommendations")
    st.caption("Top matches ranked by compatibility with your active campaign brief.")

    st.tabs(["All Matches", "Instagram", "YouTube", "TikTok"])
    matched_creators = sorted(
        st.session_state.get("matches", st.session_state["creators"]),
        key=lambda x: x.get("match_score") or 0, reverse=True,
    )
    if not matched_creators:
        st.info("No creators matched this brief. Try a different niche, a higher budget, or turn off 'Commercial use required'.")
    res_cols = st.columns(3)
    for idx, c in enumerate(matched_creators):
        with res_cols[idx % 3]:
            st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
            top_l, top_r = st.columns([3, 2])
            with top_l:
                st.image(c["avatar"], width=52)
                st.markdown(f"**{c['name']}**")
                st.caption(f"{c['handle']}")
            with top_r:
                if c.get("match_score") is not None:
                    st.markdown(f"<span class='match-pill'>{c['match_score']}% match</span>", unsafe_allow_html=True)

            st.markdown(" ".join([f"<span class='tag-pill'>{n}</span>" for n in (c.get("niches") or [])]), unsafe_allow_html=True)
            st.caption(f"👥 {c['followers']} · 📈 {c['engagement']} ER")

            for reason in (c.get("reasons") or [])[:3]:
                st.markdown(f"<span style='color:#059669;font-size:11px;font-weight:600;'>✓ {reason}</span>", unsafe_allow_html=True)
            st.write("")
            b_short, b_prof = st.columns(2)
            is_sh = c["id"] in st.session_state["shortlist"]
            if b_short.button("Shortlisted ✓" if is_sh else "Shortlist", key=f"mr_s_{c['id']}", use_container_width=True):
                if is_sh:
                    st.session_state["shortlist"].remove(c["id"])
                else:
                    st.session_state["shortlist"].add(c["id"])
                rerun_app()

            if b_prof.button("View Profile", key=f"mr_p_{c['id']}", use_container_width=True):
                st.session_state["selected"] = c
                st.session_state["page"] = "Creator Profile"
                rerun_app()
            st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 6. CREATOR PROFILE
# ==========================================
elif st.session_state["page"] == "Creator Profile":
    selected = st.session_state["selected"]

    if st.button("← Back to Matching Results"):
        st.session_state["page"] = "Matching Results"
        rerun_app()

    st.markdown("<div class='saas-card'>", unsafe_allow_html=True)
    st.image(selected["banner"], width="stretch")

    p_left, p_right = st.columns([3, 1])
    with p_left:
        st.image(selected["avatar"], width=84)
        st.markdown(f"<h3 style='margin:0;color:#0f172a;'>{selected['name']} ✓</h3>", unsafe_allow_html=True)
        st.caption(f"{selected['handle']} • {selected['location']} • Joined {selected['joined']}")
        st.markdown(" ".join([f"<span class='tag-pill'>{n}</span>" for n in (selected.get("niches") or [])]), unsafe_allow_html=True)
    with p_right:
        score = selected.get("match_score")
        if score is not None:
            st.markdown(f"<div style='text-align:center;padding:12px;background:#ecfdf5;border-radius:12px;border:1px solid #a7f3d0;'><h2 style='margin:0;color:#047857;'>{score}%</h2><span style='font-size:11px;color:#047857;font-weight:700;'>MATCH RATING</span></div>", unsafe_allow_html=True)

    st.markdown("<hr style='margin:16px 0; border:none; border-bottom:1px solid #e2e8f0;'/>", unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)
    s1.metric("Follower Base", selected["followers"])
    s2.metric("Engagement Rate", selected["engagement"])
    s3.metric("Average Views", selected["avg_views"])

    st.markdown("<hr style='margin:16px 0; border:none; border-bottom:1px solid #e2e8f0;'/>", unsafe_allow_html=True)

    st.markdown("**Creator Overview**")
    st.write(selected.get("bio") or "")

    if selected.get("reasons"):
        st.markdown("**Algorithmic Fit Drivers**")
        for r in selected["reasons"]:
            st.markdown(f"- <span style='color:#059669;font-size:12px;'>{r}</span>", unsafe_allow_html=True)

    st.markdown("**Verification**")
    v1, v2, v3 = st.columns(3)
    v1.markdown("✅ Verified tools" if selected.get("verified_tools") else "⚪ Tools not verified")
    v2.markdown("✅ Verified workflow" if selected.get("verified_workflow") else "⚪ Workflow not verified")
    v3.markdown("✅ Verified past work" if selected.get("verified_past_work") else "⚪ Past work not verified")

    if selected.get("specialization"):
        st.markdown(f"**Specialization:** {selected['specialization']}")
    if selected.get("tools"):
        st.markdown("**Tools:** " + " ".join(f"<span class='tag-pill'>{t}</span>" for t in selected["tools"]), unsafe_allow_html=True)
    if selected.get("skills"):
        st.markdown("**Skills:** " + " ".join(f"<span class='tag-pill'>{s}</span>" for s in selected["skills"]), unsafe_allow_html=True)
    if selected.get("workflow"):
        st.markdown(f"**Workflow:** {selected['workflow']}")
    if selected.get("process_evidence"):
        st.caption(f"Process evidence: {selected['process_evidence']}")

    if selected.get("portfolio"):
        st.markdown("**AI Portfolio**")
        for item in selected["portfolio"]:
            tools_used = ", ".join(item.get("tools", []))
            st.markdown(f"- **{item.get('title', 'Untitled')}** ({item.get('type', '')}): {item.get('description', '')}  \n  <span style='font-size:11px;color:#64748b;'>Tools: {tools_used}</span>", unsafe_allow_html=True)

    work = selected.get("recent_work") or []
    if work:
        st.markdown("**Recent Deliverables**")
        pw_cols = st.columns(3)
        for i, url in enumerate(work[:3]):
            pw_cols[i].image(url, width="stretch")

    st.write("")
    b_act1, b_act2 = st.columns(2)
    is_in_shortlist = selected["id"] in st.session_state["shortlist"]
    if b_act1.button("Shortlisted ✓" if is_in_shortlist else "Shortlist", use_container_width=True):
        if is_in_shortlist:
            st.session_state["shortlist"].remove(selected["id"])
        else:
            st.session_state["shortlist"].add(selected["id"])
        rerun_app()

    if b_act2.button("Initiate Outreach Channel →", type="primary", use_container_width=True):
        st.success(f"Collaboration channel initiated with {selected['name']}!")
    st.markdown("</div>", unsafe_allow_html=True)
>>>>>>> 5aa98fa6457ce71ab5be69527e98187722990b0a
