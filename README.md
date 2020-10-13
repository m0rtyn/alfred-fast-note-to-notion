<h1 align="center">Fast note to Notion (Alfred workflow)</h1>

This workflow allows you to send quick thoughts to your Notion page via Alfred.

- [Usage](#usage)
- [Setup](#setup)
  - [Install](#install)
    - [Get the workflow in Alfred](#get-the-workflow-in-alfred)
    - [Python](#python)
  - [Finding your Notion Token](#finding-your-notion-token)
    - [Finding your Notion URLs](#finding-your-notion-urls)
    - [Configure Data Files](#configure-data-files)

## Usage

You can add notes and tasks to your notion document just from Alfred app!

1. Trigger Alfred search (e.g. `option + space`)
2. Start to write: add ...
3. Select one of options: add note, add task. Or press `enter` for first result row
4. Type text of note or task
5. Press `Enter`, thats all

## Setup

There is a bit of setup required to make this project work as intended.

- Have a Notion account
- Have Alfred 4+ with access to workflows (i.e., powerpack)
- Have Python 3 installed on the system
- Have Notion document for notes
- Your Notion Token
- URLs for Several Notion Object

### Install

#### Get the workflow in Alfred

Create a Blank Workflow and dump the contents of `./alfred` sub-directory into it. If nothing change try to reload Alfred.

Or you can right click on workflow and select `Open in Finder`. In opedend window dump contents of this directory and reload Alfred.

And another option is to symlink the repository's sub-directory into the workflow directory (paths will vary in the example depending on where things are located):

```bash
ln -s ~/path/to/notion-toolbox/alfred ~/PATH_TO_ALFRED/Alfred.alfredpreferences/workflows/notion-toolbox-alfred
```

For my case i have this path to Alfred:
```bash
~/Library/ApplicationSupport/Alfred/Alfred.alfredpreferences/workflows/notion-toolbox-alfred
```

#### Python

There are certain Python dependencies that are required for the scripts to work correctly. You need to navigate to the workflow's directory so that you can execute `pip3 install -r requirements.txt` from your terminal.

Alternatively, you can manually install what is defined in the `./requirements.txt`.

### Finding your Notion Token

The first thing you'll need to do is get your Notion Token (156 character value) from your browser's cookies. 

Depending on what browser you are using this process will vary slightly. The following diagram demonstrates how to find it using Chrome on MacOS.

![](https://raw.githubusercontent.com/kevinjalbert/notion-toolbox/master/alfred/notion-token.png)

#### Finding your Notion URLs

We need to identify the Notion URL of your document with notes.

These are can be acquired by finding the correct resource in your Notion and using the Copy Link found in the context menu (i.e., right click or the left-clicking ...).

#### Configure Data Files

Given the information we've taken note of in the last 2 sections, we can now configure our data files.

- Find ./data/config.sample.json, and rename to ./data/config.json.
- Fill the value out in ./data/config.json with the Notion Token and Notion URLs:

```
  {
    "NOTION_TOKEN": "your-notion-token",
    "NOTES_PAGE_URL": "your-notion-tags-database-url",
  }
```

Note: I know that this is a rather unconventional approach for configurations with an Alfred workflow, but it is what worked best for me. Later on, I might switch it up to something more conventional.

## Acknowledgements

- 👍 Respect for [Kevin Jalbert](https://github.com/kevinjalbert)'s [Notion toolbox](https://github.com/kevinjalbert/notion-toolbox)
- Thanks to @uyouthe for repo's design advices

