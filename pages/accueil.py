import streamlit as st

st.set_page_config(page_title="ImmoEstim", page_icon="🏠", layout="wide")

st.markdown("""
<style>
    /* Fond general sombre */
    .stApp { background: #0b0f19; }

    /* HERO */
    .hero { text-align:center; padding:70px 20px 10px 20px; }
    .badge {
        display:inline-block;
        background:rgba(59,130,246,0.12);
        border:1px solid rgba(59,130,246,0.3);
        color:#60a5fa;
        padding:6px 16px;
        border-radius:999px;
        font-size:0.85em;
        font-weight:600;
        letter-spacing:0.5px;
        margin-bottom:24px;
    }
    .hero h1 {
        font-size:3.6em;
        font-weight:800;
        line-height:1.1;
        color:#f8fafc;
        margin:0 0 18px 0;
    }
    .hero h1 .grad {
        background:linear-gradient(120deg,#3b82f6,#8b5cf6,#ec4899);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }
    .hero p {
        font-size:1.2em;
        color:#94a3b8;
        max-width:640px;
        margin:0 auto;
        line-height:1.7;
    }

    /* STATS */
    .stat { text-align:center; padding:24px 10px; }
    .stat .num {
        font-size:2.6em; font-weight:800;
        background:linear-gradient(120deg,#3b82f6,#8b5cf6);
        -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    }
    .stat .txt { color:#64748b; font-size:0.8em; text-transform:uppercase; letter-spacing:1.5px; margin-top:4px; }

    /* CARTES */
    .card {
        background:linear-gradient(160deg,#141b2d,#0f1523);
        border:1px solid rgba(148,163,184,0.12);
        border-radius:20px;
        padding:32px 26px;
        height:100%;
        transition:all 0.3s ease;
        position:relative;
        overflow:hidden;
    }
    .card:hover {
        border-color:rgba(99,102,241,0.5);
        transform:translateY(-6px);
        box-shadow:0 20px 40px rgba(0,0,0,0.4), 0 0 30px rgba(99,102,241,0.15);
    }
    .card .icon-box {
        width:56px; height:56px;
        border-radius:14px;
        display:flex; align-items:center; justify-content:center;
        font-size:1.7em;
        margin-bottom:18px;
    }
    .ic-blue { background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.3); }
    .ic-violet { background:rgba(139,92,246,0.15); border:1px solid rgba(139,92,246,0.3); }
    .ic-pink { background:rgba(236,72,153,0.15); border:1px solid rgba(236,72,153,0.3); }
    .card h3 { color:#f1f5f9; font-size:1.25em; margin:0 0 10px 0; font-weight:700; }
    .card p { color:#94a3b8; font-size:0.95em; line-height:1.6; margin:0; }

    /* SECTION TITRES */
    .section-title { text-align:center; color:#f8fafc; font-size:2em; font-weight:700; margin-bottom:8px; }
    .section-sub { text-align:center; color:#64748b; margin-bottom:36px; font-size:1.05em; }

    /* ETAPES */
    .step {
        display:flex; align-items:center; gap:18px;
        background:rgba(255,255,255,0.02);
        border:1px solid rgba(148,163,184,0.1);
        border-radius:14px;
        padding:18px 22px;
        margin-bottom:14px;
    }
    .step .rond {
        background:linear-gradient(120deg,#3b82f6,#8b5cf6);
        color:white; font-weight:700;
        width:40px; height:40px; border-radius:12px;
        display:flex; align-items:center; justify-content:center;
        flex-shrink:0; font-size:1.1em;
    }
    .step .txt { color:#cbd5e1; font-size:1.05em; }

    /* FOOTER */
    .footer { text-align:center; color:#475569; padding:30px; font-size:0.9em; line-height:1.8; }
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown("""
<div class="hero">
    <div class="badge">✦ ESTIMATION PAR INTELLIGENCE ARTIFICIELLE</div>
    <h1>Connaissez la <span class="grad">vraie valeur</span><br>de votre bien immobilier</h1>
    <p>
        ImmoEstim analyse des milliers d'annonces réelles du marché parisien pour vous livrer
        une estimation fiable et instantanée. Fini les fourchettes vagues : un prix précis, en quelques secondes.
    </p>
</div>
""", unsafe_allow_html=True)

# --- CTA ---
c_g, c_c, c_d = st.columns([1.3, 1, 1.3])
with c_c:
    if st.button("🚀  Estimer mon bien", use_container_width=True):
        st.switch_page("pages/estimation.py")

st.write("")

# --- STATS ---
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown('<div class="stat"><div class="num">5 000+</div><div class="txt">Annonces analysées</div></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat"><div class="num">20</div><div class="txt">Arrondissements</div></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat"><div class="num">30 s</div><div class="txt">Par estimation</div></div>', unsafe_allow_html=True)

st.write("")
st.divider()
st.write("")

# --- POURQUOI ---
st.markdown('<div class="section-title">Pourquoi ImmoEstim ?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Simple, rapide et fiable — pensé pour vous donner une réponse claire.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="card">
        <div class="icon-box ic-blue">⚡</div>
        <h3>Instantané</h3>
        <p>Pas d'inscription, pas d'attente, pas de rendez-vous. Renseignez votre bien et obtenez son prix immédiatement.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <div class="icon-box ic-violet">🧠</div>
        <h3>Intelligence artificielle</h3>
        <p>Un modèle de machine learning entraîné sur des données réelles apprend les tendances du marché pour estimer au plus juste.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="card">
        <div class="icon-box ic-pink">🗺️</div>
        <h3>Vision cartographique</h3>
        <p>Explorez les biens sur une carte interactive de Paris et comparez les prix quartier par quartier.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()
st.write("")

# --- COMMENT CA MARCHE ---
st.markdown('<div class="section-title">Comment ça marche ?</div>', unsafe_allow_html=True)
st.write("")
c_gauche, c_milieu, c_droite = st.columns([1, 2, 1])
with c_milieu:
    st.markdown("""
    <div class="step"><div class="rond">1</div><div class="txt">Renseignez les caractéristiques de votre bien : surface, pièces, étage, DPE…</div></div>
    <div class="step"><div class="rond">2</div><div class="txt">Le modèle analyse le marché et calcule une estimation en temps réel.</div></div>
    <div class="step"><div class="rond">3</div><div class="txt">Obtenez le prix estimé ainsi que le prix au m² de votre bien.</div></div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# --- FOOTER ---
st.markdown("""
<div class="footer">
    🏠 <strong style="color:#94a3b8;">ImmoEstim</strong> — Estimation immobilière par machine learning<br>
    Projet réalisé dans le cadre du Mastère Expert en Informatique — ITIC Paris
</div>
""", unsafe_allow_html=True)