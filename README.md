# Update Module Wizard

An Odoo addon which helps developers to reduce the time needed to run a module update.

There are branches named after the major Odoo versions.
You can find a corresponding version of the module there.

[A demo on Youtube](https://youtu.be/qTxWRm-1Hxg)

> Don't take extra time to press the wizard buttons by mouse. Use `Alt+R` or `Escape` instead.

> The wizard allows you to select a module which is not installed yet. In this case you run the installation process.

## How can I update an Odoo addon?

If you develop Odoo addons, you know that module update is a very common task.

### For ~~wizards~~ sorcerers

You can restart Odoo with `-u <module name>`. There are two major cons for me.

The first one is that you need a fast, convenient way to focus the terminal where you run an Odoo instance.

The second one is that you probably need to update different addons, so you have to change the shell command frequently which takes a time (even if you're familiar with shell shortcuts).

Also if you run an Odoo instance by a task manager (from an editor or an IDE), you have to edit the tasks file every time you need to change the module name. It's a bit inconvenient. Especially if the tasks file is not ignored by Git.

Actually, it's a great way. But it's hard to optimize all the things I wrote above. Also it's worth considering misspellings.

### For human beings

You can find a module in the list of apps and update it from there. But it requires to open the home screen, then go to "Apps", then type a module name, press Enter, move the mouse cursor to the vertical ellipsis icon, press it and finally select the menu item called "Upgrade".

Also you usually need to drop the default "Apps" filter to see technical addons. But you can deal with it creating a new default filter, so it's not a problem.

It's worth mentioning that you can open the module form, press "Upgrade" and, after redirect, you can use browser history to move back to that form. But you should keep a separate tab for this purpose (1), rerender a page (2) and move your cursor to the "Upgrade" button (3!!!).

In conclusion, it is an amazing way to manage modules for administrators but not for devs.

### Run the wizard from the command panel

Now you can type a part of "Update Module" (e.g. "up mod") on the home screen to find the wizard in the command panel items. Open it. Select a module. And press "Run" (I prefer to use shortcuts). It takes several seconds.
