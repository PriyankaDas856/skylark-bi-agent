import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from pathlib import Path

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Monday AI Business Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------
css_path = Path(__file__).parent / "styles.css"

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("# 📊 Monday BI")

    st.success("🟢 Connected")

    st.markdown("---")

    st.markdown("### 💡 Try asking")

    st.markdown("""
- Executive Summary

- Deal Summary

- Work Order Summary

- Compare Sectors

- Compare Owners

- Data Quality
""")

    st.markdown("---")

    st.caption("Built with FastAPI + Streamlit")

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.markdown("""
<div class="main-title">
🚀 Monday AI Business Intelligence Agent
</div>

<div class="subtitle">
Ask natural language questions and receive instant business insights.
</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "",
    placeholder="Example: Executive Summary"
)

button = st.button("✨ Generate Insights")

# ---------------------------------------------------
# API
# ---------------------------------------------------

if button:

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("🤖 AI is analyzing your Monday workspace..."):

        try:
            API_URL = "https://skylark-bi-agent-zdeq.onrender.com/ask"

            response = requests.post(
                API_URL,
                json={"question": question},
                timeout=60
            )

        except Exception:
            st.error("Backend not running.")
            st.stop()

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    result = response.json()

    answer = result.get("answer", "")
    details = result.get("details", {})

    st.markdown(
        f"""
<div class="response-box">

### 🤖 AI Business Insight

{answer}

</div>
""",
        unsafe_allow_html=True,
    )

    if (
        isinstance(details, dict)
        and "work_orders" in details
        and "deals" in details
    ):

        work = details["work_orders"]
        deals = details["deals"]

        st.markdown("## 📈 Executive Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(
                f"""
<div class="metric-card">
<div class="metric-title">💼 Work Orders</div>
<div class="metric-value">{work['total_work_orders']}</div>
</div>
""",
                unsafe_allow_html=True,
            )

        with c2:
            st.markdown(
                f"""
<div class="metric-card">
<div class="metric-title">🤝 Deals</div>
<div class="metric-value">{deals['total_deals']}</div>
</div>
""",
                unsafe_allow_html=True,
            )

        with c3:
            st.markdown(
                f"""
<div class="metric-card">
<div class="metric-title">✅ Won Deals</div>
<div class="metric-value">{deals['deal_status'].get('Won', 0)}</div>
</div>
""",
                unsafe_allow_html=True,
            )

        with c4:
            st.markdown(
                f"""
<div class="metric-card">
<div class="metric-title">📂 Open Deals</div>
<div class="metric-value">{deals['deal_status'].get('Open', 0)}</div>
</div>
""",
                unsafe_allow_html=True,
            )

        st.divider()
                # =====================================================
        # DASHBOARD CHARTS
        # =====================================================

        left, right = st.columns(2)

        # -----------------------------
        # DEAL STATUS
        # -----------------------------

        with left:

            st.markdown("### 🥧 Deal Status")

            deal_status_df = pd.DataFrame(
                deals["deal_status"].items(),
                columns=["Status", "Count"]
            )

            fig = px.pie(
                deal_status_df,
                names="Status",
                values="Count",
                hole=0.55,
                color_discrete_sequence=px.colors.qualitative.Pastel
            )

            fig.update_layout(
                paper_bgcolor="white",
                plot_bgcolor="white",
                height=430,
                margin=dict(l=10, r=10, t=20, b=10)
            )

            fig.update_traces(
                textposition="inside",
                textinfo="percent+label"
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displaylogo": False
                }
            )

        # -----------------------------
        # WORK ORDER STATUS
        # -----------------------------

        with right:

            st.markdown("### 📦 Work Order Status")

            work_df = pd.DataFrame(
                work["execution_status"].items(),
                columns=["Status", "Count"]
            )

            fig = px.bar(
                work_df,
                x="Status",
                y="Count",
                text="Count",
                color="Status",
                color_discrete_sequence=px.colors.qualitative.Bold
            )

            fig.update_layout(
                paper_bgcolor="white",
                plot_bgcolor="white",
                height=430
            )

            fig.update_traces(textposition="outside")

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displaylogo": False
                }
            )

        st.divider()

        # =====================================================
        # SECTOR ANALYSIS
        # =====================================================

        left, right = st.columns(2)

        # -----------------------------
        # DEALS BY SECTOR
        # -----------------------------

        with left:

            st.markdown("### 🏗 Deals by Sector")

            deal_sector_df = pd.DataFrame(
                deals["sector_distribution"].items(),
                columns=["Sector", "Count"]
            )

            fig = px.bar(
                deal_sector_df,
                x="Sector",
                y="Count",
                text="Count",
                color="Count",
                color_continuous_scale="Blues"
            )

            fig.update_layout(
                paper_bgcolor="white",
                plot_bgcolor="white",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displaylogo": False
                }
            )

        # -----------------------------
        # WORK ORDERS BY SECTOR
        # -----------------------------

        with right:

            st.markdown("### 🏭 Work Orders by Sector")

            work_sector_df = pd.DataFrame(
                work["sector_distribution"].items(),
                columns=["Sector", "Count"]
            )

            fig = px.bar(
                work_sector_df,
                x="Sector",
                y="Count",
                text="Count",
                color="Count",
                color_continuous_scale="Purples"
            )

            fig.update_layout(
                paper_bgcolor="white",
                plot_bgcolor="white",
                height=450
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displaylogo": False
                }
            )

        st.divider()
                # =====================================================
        # DETAILED ANALYTICS
        # =====================================================

        with st.expander("📋 View Detailed Analytics", expanded=False):

            tab1, tab2 = st.tabs(["💼 Work Orders", "🤝 Deals"])

            with tab1:

                st.subheader("Execution Status")

                execution_df = pd.DataFrame(
                    work["execution_status"].items(),
                    columns=["Status", "Count"]
                )

                st.dataframe(
                    execution_df,
                    use_container_width=True,
                    hide_index=True
                )

                st.subheader("Sector Distribution")

                sector_df = pd.DataFrame(
                    work["sector_distribution"].items(),
                    columns=["Sector", "Count"]
                )

                st.dataframe(
                    sector_df,
                    use_container_width=True,
                    hide_index=True
                )

            with tab2:

                st.subheader("Deal Status")

                deal_df = pd.DataFrame(
                    deals["deal_status"].items(),
                    columns=["Status", "Count"]
                )

                st.dataframe(
                    deal_df,
                    use_container_width=True,
                    hide_index=True
                )

                st.subheader("Sector Distribution")

                sector_df = pd.DataFrame(
                    deals["sector_distribution"].items(),
                    columns=["Sector", "Count"]
                )

                st.dataframe(
                    sector_df,
                    use_container_width=True,
                    hide_index=True
                )

        st.divider()

    elif isinstance(details, list):

        st.subheader("📄 Results")

        st.dataframe(
            pd.DataFrame(details),
            use_container_width=True,
            hide_index=True
        )

    elif isinstance(details, dict):

        st.subheader("📄 Details")

        st.json(details)

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px;color:gray;font-size:14px;">
Built with ❤️ using
<b>FastAPI</b> • <b>Streamlit</b> • <b>Plotly</b> • <b>Monday.com GraphQL API</b>
</div>
""",
unsafe_allow_html=True
)