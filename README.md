# PalferIA Sales CRM

Internal CRM for managing sales prospects across the COM-studio and ME-sport product lines.

**Live URL:** https://sales.palferia.me  
**VPS IP:** 31.97.192.164

---

## Stack

- **Frontend:** Vanilla HTML/CSS/JS (single-file pages, no build step)
- **Auth & DB:** Supabase (JS SDK v2 via CDN)
- **WhatsApp:** OpenWA proxied by nginx at `/wa/`
- **Deploy:** GitHub Actions → rsync to VPS

---

## Setup

### 1. Supabase project

1. Go to [supabase.com](https://supabase.com) → New project.
2. In **SQL Editor**, run `supabase/schema.sql` to create tables + RLS policies.
3. Run `supabase/seed.sql` to pre-load the 17 existing prospects.
4. Go to **Project Settings → API** and copy:
   - `Project URL` → `SUPABASE_URL`
   - `anon public` key → `SUPABASE_ANON_KEY`
5. Paste both values into `public/index.html` and `public/crm.html` at the top of the `<script>` blocks (replace the `YOUR_SUPABASE_URL` / `YOUR_SUPABASE_ANON_KEY` placeholders).

### 2. Create a CRM user

In the Supabase dashboard go to **Authentication → Users → Add user** (or Invite).  
Use the email/password you'll log in with.

### 3. VPS setup

```bash
# On the VPS (as root or sudo user)

# Install nginx
apt update && apt install -y nginx

# Create web root
mkdir -p /var/www/sales.palferia.me

# Install certbot and get SSL certificate
apt install -y certbot python3-certbot-nginx
certbot --nginx -d sales.palferia.me

# Copy nginx config
cp nginx/sales.conf /etc/nginx/sites-available/sales.palferia.me
ln -s /etc/nginx/sites-available/sales.palferia.me /etc/nginx/sites-enabled/
nginx -t && systemctl reload nginx
```

### 4. GitHub Secrets

In your GitHub repo go to **Settings → Secrets and variables → Actions** and add:

| Secret | Value |
|--------|-------|
| `VPS_HOST` | `31.97.192.164` |
| `VPS_USER` | `root` (or your deploy user) |
| `VPS_SSH_KEY` | Contents of your private SSH key (`~/.ssh/id_rsa`) |

Make sure the corresponding **public key** is in `/root/.ssh/authorized_keys` on the VPS.

### 5. Deploy

```bash
git push origin main
```

GitHub Actions will rsync `public/` to `/var/www/sales.palferia.me/` automatically.

---

## Adding proposals

Drop HTML files into `public/propuestas/` and add entries to the `propuestas` array in `crm.html` (search for `const propuestas = [`).

---

## WhatsApp integration

OpenWA must be running on the VPS at port `2785`.  
Nginx proxies `/wa/` → `http://localhost:2785/` and injects the API key header automatically.  
No API key is needed in the browser JS.

---

## Color tokens

```
--cta:       #B1F727   (lime accent)
--bg-dark:   #011F29
--bg-mid:    #022A36
--bg:        #013540
--secondary: #416870
--base:      #809AA0
--iron:      #BFCCCF
--white:     #FFFFFF
```
