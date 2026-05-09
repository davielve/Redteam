import { useState } from 'react'

function App() {
  const [email, setEmail] = useState('')

  const handleBrokenClick = () => {
    // Intentionally fails only when clicked
    console.error("CRITICAL_ERROR: API Connection timeout on endpoint /v1/waitlist/join")
    throw new Error("UI_CRASH: React state corrupted by invalid null response")
  }

  return (
    <div className="container">
      <nav className="navbar">
        <div className="logo">SaaS Pro</div>
        <div className="links">
          <a href="#">Product</a>
          <a href="#">Pricing</a>
          <a href="#">About</a>
          <button className="nav-cta">Get Started</button>
        </div>
      </nav>

      <main className="hero">
        <h1>Scale your business with AI.</h1>
        <p className="subtitle">The only platform you'll ever need to manage everything.</p>
        
        <div className="card signup-card">
          <h2>Create your free account</h2>
          <div className="form-group">
            <input 
              type="text" 
              placeholder="Email" 
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <button onClick={handleBrokenClick} className="btn-primary">
            Join the waitlist
          </button>
        </div>

        <div className="accessibility-fail">
          <button style={{ backgroundColor: '#eee', color: '#fff' }}>
            Ghost Button
          </button>
        </div>
      </main>

      <section className="mobile-broken">
        <div className="mobile-only-nav" style={{ display: 'none' }}>
          <div className="burger" onClick={() => { throw new Error("Mobile menu crash") }}>Menu</div>
        </div>
      </section>

      <footer>
        <p>&copy; 2024 SaaS Pro Inc.</p>
        <a href="#" style={{ fontSize: '1px' }}>Secret Link</a>
      </footer>
    </div>
  )
}

export default App
