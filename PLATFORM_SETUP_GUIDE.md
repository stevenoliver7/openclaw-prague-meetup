# Platform Setup Guide

## Meetup.com Setup
### Prerequisites
- A registered Meetup.com user account.
- A credit card (Meetup requires a paid Organizer subscription to host groups and events).
- A square logo/image for the group and a 16:9 cover image for the event.

### Step-by-Step
1. **Create a New Group**: Go to Meetup.com and click **Start a new group**. Name it "OpenClaw Prague" (Meetup operates on a Group > Event hierarchy; you must create a group first).
2. **Set Group Location & Category**: Enter "Prague, Czech Republic". Select "Technology" as the primary topic.
3. **Add Tags**: Add the following topics to help Meetup's algorithm find members: *AI, open source, developers, machine learning*.
4. **Draft the Group Description**: Keep it brief. "A community for open-source AI tinkerers in Prague setting up the OpenClaw ecosystem." 
5. **Start Your Subscription**: Choose the standard organizer subscription (monthly or 6-month billing).
6. **Create the Event**: On your new group page, click **Create event**.
7. **Fill in Details**: 
   - **Title**: *OpenClaw Prague Meetup #1 — The AI Meetup That Doesn't Suck 🐱*
   - **Date & Time**: Thursday, March 26, 2026, 18:00 - 21:00 CET.
   - **Description**: "First OpenClaw community meetup in Europe. Open-source AI tinkerers sharing what they've built. Talks, hands-on building, good beer. No suits, no sales pitches. Website: https://openclawprague.cz | Telegram: https://t.me/+openclaw"
8. **Set Location to TBD**: Choose "In person". Instead of a specific address, toggle or type "To be announced" (you will update this once the venue is confirmed).
9. **Configure RSVP Settings**:
   - **Price**: Free
   - **Attendee Limit**: 50
   - **Waitlist**: Enable (automatic)
   - **Guests**: Allow 1 per person.
10. **Publish**: Click **Publish** to make the event live to the Meetup network.

### Costs
- **Organizer Subscription**: ~$15 to $30 per month depending on the billing cycle (Standard tier). Required to host the group.
- **Event Cost**: $0 (Free events don't incur ticketing fees).

### Tips
- **Send a venue update**: When you secure a venue, update the event location and use the "Contact attendees" tool to email everyone the exact address.
- **Leverage the network**: Meetup.com will automatically email locals interested in AI. This is the main reason to pay the monthly fee.

---

## Luma Setup
### Prerequisites
- A Luma account (create one at lu.ma using your email or Google account).
- A 16:9 banner image (event cover).

### Step-by-Step
1. **Create Event**: Go to your Luma dashboard and click **Create Event**.
2. **Basic Info**: 
   - **Event Name**: *OpenClaw Prague Meetup #1 — The AI Meetup That Doesn't Suck 🐱*
   - **Start & End Time**: March 26, 2026, 6:00 PM to 9:00 PM (CET).
3. **Location**: Select "In Person". Type "Prague, Czechia" as the general location. You can add a note in the location details saying "Exact venue TBD - will be emailed to RSVPs."
4. **Event Page Design**: Upload your banner image. Keep the rich text description identical to the Meetup one (mention the no suits/sales pitches rule and link to the Telegram group).
5. **Registration Settings**: 
   - Go to the **Settings** tab.
   - **Capacity**: Set a strict limit of 50.
   - **Waitlist**: Enable (waitlisted people will automatically be offered a spot if someone cancels).
   - **Approval**: Set to "Auto-Approve" to reduce friction, as this is an open community event.
6. **Publish**: Click **Publish** in the top right.
7. **Automated Emails**: Go to the **Emails** tab to preview or customize the automatic reminder email Luma sends 24 hours before the event.

### Costs
- **Luma Pricing**: $0. Luma is completely free to use for free events, with no hidden limits on attendees or emails.

### Tips
- **Keep custom questions minimal**: Don't force users to fill out long forms. Just ask for their Name and Email (default). Optionally ask for "Company/Project" if you are printing name tags.
- **Calendar invites**: Luma automatically sends beautiful calendar invites with the RSVP confirmation.

### Website Embed
To embed the Luma registration directly onto https://openclawprague.cz:
1. Go to your published Luma event dashboard.
2. Click on the **Share** button (top right).
3. Select **Embed on Website**.
4. Copy the provided HTML `<iframe ...>` code.
5. Paste this code directly into your `index.html` file where you want the RSVP button or ticketing widget to appear.

---

## Recommendation
**Start exclusively with Luma.** It is completely free, looks much more modern, caters exactly to the tech/startup crowd, and embeds effortlessly into your website. 

Only use Meetup.com if you launch the Luma link to your Telegram/network and fail to reach the 50-person capacity. Meetup's only true advantage is its algorithmic discovery for locals browsing the app, but it comes with a $15-$30 monthly tax. If you can fill 50 seats yourself via Twitter, Telegram, and word-of-mouth, Meetup.com is an unnecessary expense.