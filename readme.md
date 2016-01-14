# WriteNow

[WriteNow][writenow] is a social writing application by [Allan Lasser][me].
It's like newsletters, but backwards.
Individually respond to writing prompts, then read everyone else's responses.
It was conceived at the [CODEX Hackathon][codex] in 2016.

## Purpose

I like newsletters.
I like that they're emails.
I like that they stay in my inbox.
It gets me to actually read them.
And there's a personability, an informality, that is informed by its context.
I feel like I'm being written _to_, rather than _for_.
Newsletters, as a format, are rising in popularity, and justifiably so.

These days we are writing more than ever.
Between all the texts, tweets, and emails we send to one another, we're writing enough to fill volumes.
So I wanted to piggy-back on that behavior.
I also wanted something that captured those positive feelings, but in the opposite direction.
A newsletter is written by one person and sent to many people.
What if we could have many writers send their writing all to the same place?

I want us all to write about the same thing, to capture the range of voices that surrounds any one subject.
I want that writing to come naturally.
I want it to fit into the daily flow, to allow us to sneak some expression into an otherwise utilitarian routine.
These likes and wants gave rise to this, WriteNow.
It's a way for writers to respond to prompts and then see all the results in one place.

So that's what this is and why it exists.

## Goals

1. Create a simple and straightforward system for collaborative writing.
2. Use email as the primary interactive interface.
3. Allow the system to be used _without_ registering for an account.
4. Afford privacy, accessibility, and utility, while fostering community.

## Specification

A **group** is a collection of authors and a collection of prompts.
Every group has a corresponding email address.

An **author** can join any group by entering their email and a name.
The email is kept private and only used by the system.
The name is used to identify authorship of an individual response within a group.

A **prompt** is created by sending an email to the group's email address.
If the sender is a member of the group, then the prompt is sent out to all members of the group.
Every prompt has a corresponding email address.

A **response** is created by sending an email to the prompt's email address.
If the sender is a member of the group, then their response is recorded.
The body of the email is used to create the response.

### URL Structure

<table>
    <thead>
        <tr>
            <th>Path</th>
            <th><code>GET</code></th>
            <th><code>POST</code></th>
        </tr>
    <tbody>
        <tr>
            <td><code>groups/</code></td>
            <td>Displays all the writing groups</td>
            <td>Creates a new group</td>
        </tr>
        <tr>
            <td><code>groups/<b>group</b>/</code></td>
            <td>Displays the group's prompts and authors</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><code>groups/<b>group</b>/join</code></td>
            <td>Displays a form for adding an email to the group</td>
            <td>Adds email to the group</td>
        </tr>
        <tr>
            <td><code>groups/<b>group</b>/leave</code></td>
            <td>Displays a form for removing an email from the group</td>
            <td>Removes email from the group</td>
        </tr>
        <tr>
            <td><code>groups/<b>group</b>/<b>author</b></code></td>
            <td>Displays the author's responses within the group</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><code>prompts</code></td>
            <td>Displays all of the prompts</td>
            <td>Creates a new prompt</td>
        </tr>
        <tr>
            <td><code>prompts/<b>prompt</b></code></td>
            <td>Displays all the responses to that prompt</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td><code>prompts/<b>prompt</b>/<b>response</b></code></td>
            <td>Displays a single response</td>
            <td>N/A</td>
        </tr>
    </tbody>
</table>

### Data Structure

```
{
    Group: {
        id: Int,
        name: String,
        email: String,
        authors: List[Author],
        prompts: List[Prompt],
    },
    Author: {
        id: Int,
        name: String,
        email: String
    },
    Prompt: {
        id: Int,
        date: Date,
        email: String,
        title: String,
        body: String,
        author: Writer
    },
    Reponse: {
        id: Int,
        date: Date,
        title: String,
        body: String,
        author: Writer
    }
}
```

[writenow]: http://writenow.email/
[codex]: http://codexhackathon.com/
[worb]: http://worb.co/
[me]: http://www.allanlasser.com/
