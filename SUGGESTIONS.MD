## Feedback on Greptile API

1. **Consistency in Response**: Greptile is highly consistent with its responses, rarely hallucinating and providing the same output for identical inputs. While consistency is a strength, it can also be a limitation. The responses from Greptile can be stubborn and inflexible, making it difficult to manipulate the data into the desired format. Introducing options to adjust or fine-tune response formatting could enhance user control.

2. **Repository Management**: A feature to delete indexed repositories.

3. **Local Codebase Access**: Expanding the API’s capabilities to include access to local codebases, beyond GitHub and GitLab.

### Some Low-Hanging Improvements:

4. **SDK Availability**

5. **Distance Parameter Explanation**: The `/query` endpoint returns a `distance` parameter that lacks explanation in the documentation. 

6. **Reload and Notify Parameters**: The `reload` and `notify` parameters in the `/repositories` endpoint are not sufficiently explained. 

7. **Query Speed**: The `/query` endpoint seems slightly slow at times (take this with a grain of salt, might be a mistake from my side)