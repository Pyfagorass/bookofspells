# Suggested Prompts for MojoAuth OIDC — Next.js

## Full Implementation

> "Add passwordless authentication to my Next.js (App Router) application using MojoAuth.
>
> Follow `skills/authentication/oidc-hosted-page-nextjs/SKILL.md` exactly.
>
> Requirements:
> 1. Install `openid-client` and configure the OIDC Issuer in a server-side utility.
> 2. Create a login page with a 'Sign In with MojoAuth' button.
> 3. Create an API route (`/api/auth/login`) that initiates the OIDC redirect to MojoAuth Hosted Login Page.
> 4. Create a callback API route (`/api/auth/callback`) that exchanges the code for tokens and creates a session.
> 5. Handle errors and redirect back to login with a message on failure.
>
> My MojoAuth config:
> - MojoAuth Domain: `your-app.mojoauth.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:3000/api/auth/callback`"

## Add MojoAuth to Existing Login

> "My Next.js app uses NextAuth / credentials login. Add MojoAuth as an alternative passwordless sign-in method.
> Reference the skill file at `skills/authentication/oidc-hosted-page-nextjs/SKILL.md`.
> Keep both password and MojoAuth login working side by side."
