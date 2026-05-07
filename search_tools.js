const { execSync } = require('child_process');
const payload = {
    queries: [{ use_case: 'create a github repository' }],
    session: { generate_id: true }
};
try {
    const jsonString = JSON.stringify(payload);
    // On Windows, double quotes inside the string need to be escaped for the shell
    const escapedJson = jsonString.replace(/"/g, '\\"');
    const command = `accio-mcp-cli call COMPOSIO_SEARCH_TOOLS --json "${escapedJson}"`;
    const output = execSync(command).toString();
    console.log(output);
} catch (e) {
    console.log(e.stdout ? e.stdout.toString() : e.message);
}
