import React from 'react';
import './HomePage.css';

function BibleVerseCard() {
  return (
    <div className="bible-verse">
      <div className="bible-verse-header">A Message of Love</div>
      Love is patient, love is kind. It does not envy, it does not boast, it is not proud. It does not dishonor others, it is not self-seeking, it is not easily angered, it keeps no record of wrongs. Love does not delight in evil but rejoices with the truth. It always protects, always trusts, always hopes, always perseveres.
      <span className="bible-verse-ref">1 Corinthians 13:4-7</span>
    </div>
  );
}

function VenueInfo() {
  return (
    <div className="venue" style={{marginTop:32, position:'relative', zIndex:1}}>
      <div style={{textAlign:'center'}}>
        <strong>Venue:</strong> Victory Family Centre Tampines (Level 3)<br />
        <strong>Address:</strong> 20 Tampines Street 43, Singapore 529151
      </div>
      {/* Images would use public folder or import statements in React */}
      <img src="/static/couple_pic1.png" alt="Couple Photo" className="couple-photo-art" title="Joel & Amanda" />
      <img src="/static/vfc.png" alt="Venue Photo" className="venue-photo-art" title="Victory Family Centre Tampines" />
    </div>
  );
}

function RSVPButton() {
  return (
    <a href="/rsvp" className="btn">RSVP Now</a>
  );
}

function EventDetailsCard() {
  return (
    <div className="event-details-card" style={{background:'#fff', borderRadius:'1.5rem', boxShadow:'0 2px 12px rgba(214,51,108,0.08)', padding:'24px', margin:'32px auto', maxWidth:'500px', textAlign:'left', display:'flex', flexDirection:'column', gap:'18px'}}>
      <div style={{display:'flex', alignItems:'center', gap:'12px'}}>
        <span style={{fontSize:'2rem'}}>📍</span>
        <span><strong>Venue:</strong> Victory Family Centre Tampines (Level 3)</span>
      </div>
      <div style={{display:'flex', alignItems:'center', gap:'12px'}}>
        <span style={{fontSize:'2rem'}}>🏠</span>
        <span><strong>Address:</strong> 20 Tampines Street 43, Singapore 529151</span>
      </div>
      <div style={{display:'flex', alignItems:'center', gap:'12px'}}>
        <span style={{fontSize:'2rem'}}>📅</span>
        <span><strong>Date:</strong> November 29</span>
      </div>
      <div style={{display:'flex', alignItems:'center', gap:'12px'}}>
        <span style={{fontSize:'2rem'}}>⏰</span>
        <span><strong>Start Time:</strong> 2:00 PM</span>
      </div>
    </div>
  );
}

export default function HomePage() {
  return (
    <div className="container">
      <h1>Joel & Amanda's Wedding</h1>
      <h2>You're Invited!</h2>
      <EventDetailsCard />
      <RSVPButton />
      <BibleVerseCard />
      <VenueInfo />
    </div>
  );
}
