# ArcherPhish
This is a demo/research project intended to aid in the understanding of advanced phishing attacks used by adversaries, based upon the preliminary research/notes in this microsoft article: https://www.microsoft.com/security/blog/2022/07/12/from-cookie-theft-to-bec-attackers-use-aitm-phishing-sites-as-entry-point-to-further-financial-fraud/

The PoC here works on a a very basic site that I created.  The server is setup to retrieve web pages for a hardcoded destination, and print the credentials used along with authentication cookies to the terminal.  This is extremely basic, and doesn't offer support for SSL, and may have issues with fully custom enterprise-level websites.
