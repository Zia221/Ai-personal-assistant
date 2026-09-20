import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =========================================
           GLOBAL
        ========================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at top right,
                    rgba(99, 102, 241, 0.12),
                    transparent 30%
                ),
                #0b0f19;
        }


        /* =========================================
           HIDE STREAMLIT DEFAULT UI
        ========================================= */

        #MainMenu {
            visibility: hidden;
        }

        footer {    
            visibility: hidden;
        }

     


        /* =========================================
           SIDEBAR
        ========================================= */

        section[data-testid="stSidebar"] {
            background: #0f1420;
            border-right: 1px solid #1f2937;
        }

        section[data-testid="stSidebar"] > div {
            padding-top: 1.5rem;
        }


        /* =========================================
           BRAND
        ========================================= */

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 4px 24px 4px;
        }

        .brand-icon {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(
                135deg,
                #6366f1,
                #8b5cf6
            );
            font-size: 22px;
        }

        .brand-title {
            font-size: 18px;
            font-weight: 700;
            color: #f8fafc;
        }

        .brand-subtitle {
            font-size: 11px;
            color: #94a3b8;
            margin-top: 2px;
        }


        /* =========================================
           ONLINE STATUS
        ========================================= */

        .status {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(34, 197, 94, 0.08);
            border: 1px solid rgba(34, 197, 94, 0.2);
            border-radius: 20px;
            padding: 5px 10px;
            color: #86efac;
            font-size: 12px;
        }

        .status-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #22c55e;
        }


        /* =========================================
           PAGE HEADER
        ========================================= */

        .page-header {
            padding: 20px 0 10px 0;
        }

        .page-title {
            font-size: 30px;
            font-weight: 750;
            color: #f8fafc;
            letter-spacing: -0.5px;
        }

        .page-subtitle {
            color: #94a3b8;
            font-size: 14px;
            margin-top: 4px;
        }


        /* =========================================
           CHAT
        ========================================= */

        .chat-user {
            background: #171d2b;
            border: 1px solid #263043;
            border-radius: 18px 18px 4px 18px;
            padding: 14px 18px;
            margin: 8px 0 16px auto;
            max-width: 78%;
            color: #e2e8f0;
        }

        .chat-assistant {
            background: #111827;
            border: 1px solid #243044;
            border-radius: 18px 18px 18px 4px;
            padding: 14px 18px;
            margin: 8px auto 16px 0;
            max-width: 82%;
            color: #e2e8f0;
        }


        /* =========================================
           AGENT BADGE
        ========================================= */

        .agent-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.25);
            color: #a5b4fc;
            padding: 4px 9px;
            border-radius: 8px;
            font-size: 11px;
            margin-bottom: 8px;
        }


        /* =========================================
           WELCOME CARD
        ========================================= */

        .welcome-card {
            text-align: center;
            padding: 60px 30px 40px 30px;
        }

        .welcome-icon {
            font-size: 52px;
            margin-bottom: 12px;
        }

        .welcome-title {
            font-size: 30px;
            font-weight: 750;
            color: #f8fafc;
        }

        .welcome-text {
            color: #94a3b8;
            font-size: 15px;
            margin-top: 8px;
        }


        /* =========================================
           DASHBOARD CARDS
        ========================================= */

        .dashboard-card {
            background: #111827;
            border: 1px solid #243044;
            border-radius: 16px;
            padding: 18px;
            height: 100%;
        }

        .card-icon {
            font-size: 24px;
        }

        .card-title {
            color: #f8fafc;
            font-weight: 650;
            margin-top: 10px;
        }

        .card-description {
            color: #94a3b8;
            font-size: 13px;
            margin-top: 5px;
        }


        /* =========================================
           SECTION TITLE
        ========================================= */

        .section-title {
            color: #f8fafc;
            font-size: 19px;
            font-weight: 700;
            margin: 24px 0 12px 0;
        }


        /* =========================================
           METRIC CARDS
        ========================================= */

        .metric-card {
            background: #111827;
            border: 1px solid #243044;
            border-radius: 14px;
            padding: 16px;
        }

        .metric-label {
            color: #94a3b8;
            font-size: 12px;
        }

        .metric-value {
            color: #f8fafc;
            font-size: 25px;
            font-weight: 750;
            margin-top: 5px;
        }


        /* =========================================
           MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .page-title {
                font-size: 24px;
            }

            .chat-user,
            .chat-assistant {
                max-width: 95%;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )