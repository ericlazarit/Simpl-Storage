# Simpl Storage

> A Discord bot that turns your server into a smarter, searchable file-transfer hub.

## Why this discord bot?

It is rather laborious to transfer files between devices. Either you have to open dropbox or Googlle Drive or some sort of AirDrop system. It is often easier for you to drop a file in your discord chat so that you can easily open up discord on your other device so that you can access it.

However, this method of file tranfer faces a few challenges. First, the manner in which you search for an old file is very limited so you are often left scrolling and looking at file previews or file names manually since discord's native search function does not allow either methods of search.

Therefore, this bot/application serves to remedy this problem. Additionally, it still serves as a quick-drop method of file transfer aswell as adding robust features alongside including, a more advanced search that allows lookups by Filename, File type, Upload Date and file size in a more user-friendy interface. No more scrolling ad infinitum!

## Features

- [ ] Upload files via Discord chat and auto-index them
- [ ] Search by filename (partial match supported)
- [ ] Filter by file type (e.g. `.pdf`, `.png`, `.zip`)
- [ ] Filter by upload date / date range
- [ ] Filter by file size
- [ ] Simple, user-friendly command interface (slash commands)

## Tech Stack

- **Bot:** Python 3.11+ with [discord.py](https://discordpy.readthedocs.io/)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** SQLite
- **Frontend:** React dashboard

## Project Structure

```
simpl-storage/
├── bot/            # Discord bot (discord.py)
├── backend/        # FastAPI backend + SQLite database
├── frontend/       # React dashboard
└── README.md
```

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/simpl-storage.git
cd simpl-storage
```

### Bot + Backend (Python)

```bash
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Frontend (React)

```bash
cd frontend

# Install dependencies
npm install
```

## Configuration

Create a `.env` file inside `backend/`:

```env
DISCORD_TOKEN=your_bot_token_here
DATABASE_URL=sqlite:///./simpl_storage.db
```

## Usage

Run the FastAPI backend (and Discord bot, if run from the same process):

```bash
cd backend
uvicorn main:app --reload
```

Run the React dashboard:

```bash
cd frontend
npm run dev
```

Once the bot is running and invited to your server, drop a file into any channel it has access to — it'll automatically index it. Use the search commands to find it later, or use the React dashboard to browse and search visually:

```
/search filename:report
/search type:pdf
/search after:2026-01-01 before:2026-06-01
/search size:>10mb
```

_(Exact command syntax subject to change as the project develops.)_

## Roadmap

- [ ] Core file indexing
- [ ] Search command suite
- [ ] Pagination / embed-based results UI
- [ ] Optional per-user or per-channel file scoping
- [ ] Duplicate file detection
- [ ] React dashboard: file browser + search UI
- [ ] FastAPI endpoints for search/filtering

## Contributing

Issues and pull requests are welcome. If you have ideas for search filters or UX improvements, open an issue to discuss.

## License

_TBD_
