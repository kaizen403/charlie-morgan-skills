# client-onboarding-contracts

*Original trigger description:* Use whenever onboarding a new client, designing an onboarding sequence, building an integration checklist, drafting a services agreement / contract template, choosing a contract software (DocuSign etc.), structuring the post-sale handoff, deciding payment-then-contract-then-onboarding order, debugging buyer's remorse and "180s" after the sale, building the SOP for a virtual assistant to onboard clients, or whenever someone asks "I just closed a client, what now?". Also load when designing the bridge between sales and delivery, especially for service businesses, agencies, and consultancies.

---

# Client Onboarding & Contracts

> "Take the payment first. Then send the contract. Then send the onboarding. Never, ever, ever in any other order. Get this wrong and you will get 180s, refunds, and ghosting."

## When to use

Load this skill the moment a client has said yes on a sales call. Also load when designing onboarding workflows, training a VA to handle onboarding, building integration checklists, drafting service agreements, or answering "how do I move someone from sale to service smoothly?"

Sister skills: `imperium-conversion-playbook` (the close that precedes onboarding), `virtual-assistant-masterclass` (for offloading onboarding ops), `team-management-basics` (for SOPs).

---

## The Iron Order: Payment → Contract → Onboarding

This sequence is non-negotiable, learned across thousands of client signups. Doing it in any other order introduces friction and doubt that kills the deal *after* the verbal yes.

### Step 1 — Payment (on the call, before anything else)

- Take payment **on the sales call**, before sending any contract or onboarding material.
- Send a payment link (PayFunnel, Stripe Checkout, etc.) or take card details over the phone. Most business owners are perfectly comfortable giving card details verbally for a service they have just been sold.
- Watch Stripe / processor in real time and confirm receipt of payment before moving on.
- If the payment fails:
  - Ask them to retry the original link.
  - Ask them to check email/SMS for a bank fraud alert.
  - Try a smaller amount via custom link to get something through.
  - If still blocked: secure a $100 deposit OR ask for a bank transfer for the full amount.
  - Schedule a specific date/time to retry the charge in Stripe.

**Why payment first?** If you don't get the money first, the contract scares them, the onboarding overwhelms them, and "I'll get back to you" appears. The friction of any post-call admin step compounds. Payment first locks in the commitment psychologically.

> "We do not invoice pro rata. We do not do the work and then wait for payment. You will not get paid. This is digital business."

### Step 2 — Contract (immediately after, still on the call or seconds after)

- Send a **DocuSign** services agreement while you are still on the Zoom call (or immediately after).
- Tell the client: "I'm sending the agreement to your email now. Sign it before end of business today. I'll send the onboarding material tomorrow morning."
- The contract should be templated in DocuSign with yellow-highlighted fields you customize per client (name, addresses, scope, fees).
- Keep a downloaded copy on your computer in case a prospect ever asks to see the contract before payment (rare).
- If the contract has a **guarantee**, include it explicitly in the contract. Don't keep it as verbal commitment. (See `guaranteeing-results`.)
- Address contract-related questions yourself — they are a client now, not a prospect. You should know your contract inside and out.

**Why contract second?** It legally locks the deal, protects both parties, and sets the rails for delivery. Sending it before payment lets buyer's remorse intervene.

### Step 3 — Onboarding / Integration Checklist (next morning, never same day)

- Wait until the **next morning** to send the onboarding/integration checklist.
- If the client asks why: "We have an internal meeting about every client before giving access. New accounts are created next-AM."
- The real reason is psychological: **forcing them to sleep on the decision lets it solidify.** Overnight, they convince themselves it was the right call. By morning, they're excited rather than overwhelmed.
- If you slam them with the onboarding checklist immediately after taking payment, you risk overwhelm → panic → 180 → refund request.

> "By letting them sleep on the decision, they wake up thinking it's the right decision. Immediate access or immediate onboarding will mess with the psychological buy-in confirmation."

This single move drastically reduces refund / chargeback / ghost-after-sale incidents.

---

## The Integration Checklist (build this once, reuse forever)

Your integration checklist is the single document that tells a new client every action they must take so you can do your job. Build it once, deliver it perfectly every time.

### How to build the checklist

1. **List everything you need.** Software access, account permissions, asset uploads, brand info, target audiences, communication channels, ad account access, page admin permissions, customer info, internal credentials. Anything you would ever need to do your work.
2. **Sequence it.** Convert the list into linear, numbered steps: 1, 2, 3 ... Each step contains exactly one action.
3. **Format it cleanly in a Google Doc.** With detailed written instructions for each step.
4. **Record a screen-share video.** Walk through every step on camera. Don't assume the client knows how to grant Facebook ad account access or share a Google Drive folder — half of them don't. Embed the video at the top of the doc.
5. **Set a timeframe expectation.** "We aim to complete onboarding within 48 hours of contract signing. Once the checklist is done, we will start work within X business days."
6. **Make signing the contract part of the checklist.** First item: confirm contract signed.

### Example items (B2B agency, gym niche)

- Agreement on the lead magnet and offer.
- Set up Mailchimp / autoresponder.
- Set up CRM (Leadowl etc.).
- Set up Zapier integrations.
- Set up Calendly with booking link.
- Provide Facebook page admin access + ad account ID.
- Upload professional gym photos to a shared Google Drive.
- Provide testimonials, transformations, success stories, ad copy raw material.
- Define unique selling point in writing.
- Identify competitors.
- Define target customer / geo radius.
- Confirm communication channel (default: WhatsApp Business).

Yours will look completely different. The pattern is what transfers, not the items.

### Software costs

Some onboarding requires paid third-party software. Two ways to handle:
- **Client pays:** make this clear up front. Most are happy to pay small SaaS fees if you've justified value.
- **You pay:** finesse the cost into your pricing.

Either is fine. Just be transparent.

---

## Communication Channel Default: WhatsApp Business

Use **WhatsApp Business** for client communication unless you have a specific reason not to.

- Most international and SMB clients already use it.
- It's intimate, fast, low-friction.
- A client with a problem will WhatsApp before they email. Email-only clients ghost when problems arise.
- If you're in the US: iMessage or WhatsApp Business — whichever your clients actually use.

The principle: pick the channel that requires the **least cognitive load** for them to ping you. A frustrated client who has to write an email will usually just churn instead.

---

## Contract Template Essentials

Charlie's template (use as a starting point — get a lawyer to review for your jurisdiction):

- Parties (you / your company, the client).
- Services description (specific deliverables — not vague).
- Term length.
- Fees and payment terms.
- Performance guarantee (if applicable — paste this in deliberately, don't leave verbal).
- Termination conditions.
- Refund policy (or explicit "no refunds" with reason).
- Confidentiality / IP clauses.
- Limitation of liability.
- Governing law.

**Fields to customize per client (highlight in yellow):** company name, signing party, dates, fees, scope, target outcomes, any guarantee numbers.

> "These are not legal advice. Always consult a qualified lawyer before using templated legal documents."

---

## Three-Step Onboarding Recap

```
SALES CALL  →  PAYMENT (on call, Stripe/PayFunnel)
            →  CONTRACT (DocuSign, signed today)
            →  ONBOARDING CHECKLIST (next morning, video + Google Doc)
            →  CLIENT COMPLETES CHECKLIST
            →  YOU START WORK
```

That is the entire bridge between sale and delivery. Build it once, run it every client.

---

## Common Pitfalls

- **Sending the contract before payment.** The contract scares them. Always payment first.
- **Sending onboarding the same day as the sale.** Triggers overwhelm → 180. Always wait until next morning.
- **No video walkthrough on the integration checklist.** The client gets stuck on step 4, doesn't ask, and you sit waiting for ad account access for two weeks. Always record the video.
- **Net-30 invoicing.** You will not get paid consistently. Always charge upfront for service businesses.
- **Email-only client communication.** Clients churn faster when communication is high-friction. Use WhatsApp.
- **Verbal-only guarantees.** Always written into the contract.

---

## Hand-off to a VA

Once you have the integration checklist and contract templated, this entire workflow is something a virtual assistant can handle (see `virtual-assistant-masterclass`). The VA's SOP:

1. After the closer marks "deal closed" in the CRM:
2. Send the DocuSign template, customized.
3. Track signature in DocuSign.
4. The next morning, send the integration checklist Google Doc + walkthrough video.
5. Follow up daily until the checklist is complete.
6. Notify the delivery team when complete.

This is a 5-step SOP. Document it once. Hand it over. Reclaim 5–10 hours per close.

---

## Source

- Transcriptions/week6/6_3__client_onboarding___contracts.txt — the full payment-contract-onboarding sequence, the integration checklist build, the next-morning psychology, the WhatsApp default, the contract template structure, the three-step process.
