import React from 'react';
import ProfileCards from './ProfileCard';

const ContactUs = () => {
    return (
        <div>
            <h1>Contact Us</h1>
            <p>Send us a message!</p>
            <ProfileCards name="John Doe" age="25" role="Software Engineer" imagg="https://randomuser" />
            <ProfileCards name="Jane Doe" age="22" role="Web Developer" imagg="https://randomuser.me/api/portraits" />
            <ProfileCards name="John Smith" age="30" role="Data Analyst" imagg="https://randomuser.me/api/portraits" />

        </div>
    );
}

export default ContactUs;