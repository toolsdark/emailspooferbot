<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>EmailSender Bot</title>
</head>
<body>
    <h1>EmailSender Bot</h1>

    <a href="LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
    </a>

    <p>Welcome to EmailSender Bot, a powerful and versatile tool for sending emails effortlessly. Whether you need to send newsletters, notifications, or personalized messages, our bot has you covered.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Simplicity:</strong> Send emails with just a few lines of code or through an easy-to-use web interface.</li>
        <li><strong>Customization:</strong> Personalize your emails with dynamic content and variables.</li>
        <li><strong>Templates:</strong> Create and reuse email templates for consistent messaging.</li>
        <li><strong>Attachments:</strong> Send files and attachments with your emails.</li>
        <li><strong>Scheduled Sending:</strong> Schedule emails to be sent at specific times.</li>
        <li><strong>Logging:</strong> Keep track of all sent emails for reference and auditing.</li>
        <li><strong>Multiple Providers:</strong> Supports various email providers, including SMTP, SendGrid, and more.</li>
    </ul>

    <h2>Getting Started</h2>
    <ol>
        <li>
            <strong>Installation:</strong>
            <pre><code>npm install emailsender-bot</code></pre>
        </li>
        <li>
            <strong>Usage:</strong>
            <pre><code>const EmailSender = require('emailsender-bot');

const sender = new EmailSender({
  provider: 'smtp', 
  apiKey: 'YOUR_API_KEY',
});

sender.sendEmail({
  to: 'recipient@example.com',
  subject: 'Hello, World!',
  text: 'This is a test email sent from EmailSender Bot.',
});</code></pre>
        </li>
    </ol>

    <h2>Documentation</h2>
    <p>Explore our documentation for in-depth information on usage, options, and best practices.</p>

    <h2>Support</h2>
    <p>If you have any questions, encounter issues, or need assistance, please feel free to <a href="https://github.com/emailsender-bot/issues">open an issue</a>.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Get Started</h2>
    <p>Get started with EmailSender Bot today and supercharge your email communications. Visit our <a href="https://t.me/tooldark_bot">Telegram</a> for more information and pricing details.</p>
</body>
</html>
