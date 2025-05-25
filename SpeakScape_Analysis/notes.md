## Column Selection Rationale for the Combined TED Dataset

### Project Focus
SpeakScape aims to deliver **content-focused, data-driven feedback** by analyzing linguistic patterns in presentation transcripts. To ensure relevance, we curated a combined dataset based on TED_2017 and TED_2020, with a strong emphasis on **textual quality** and **engagement prediction**. This guided our column selection strategy.

### Why We Dropped Certain Columns
To streamline analysis and improve model performance, we excluded columns that were:
- **Irrelevant to textual content** (e.g., platform metadata, media URLs)
- **Highly incomplete or noisy** (e.g., nested ratings, related content)
- **Redundant or derivable** (e.g., name duplicates, count fields)

This helped us reduce data complexity and focus only on **linguistic and engagement-critical features**.

### Cleaning Results
We dropped records with missing or too-short transcripts:
- **TED_2017**: 2,549 original → 2,453 cleaned (3.8% excluded)
- **TED_2020**: 4,589 original → 4,076 cleaned (11.2% excluded)

### Retained Core Columns
| Column           | Purpose                                               |
|------------------|--------------------------------------------------------|
| `title`          | Presentation title for reference/context               |
| `transcript`     | Primary input for NLP and linguistic analysis          |
| `description`    | Secondary contextual content                           |
| `speaker`        | Attribution, used for future personalization           |
| `tags`           | Topic categorization                                   |
| `views`          | Proxy for engagement (label or regression target)      |
| `recorded_date`  | Used for temporal trends and analysis                  |
| `event`, `duration` | Presentation context and time budget                |

These columns are **well-populated**, **aligned with our research goals**, and **suitable for machine learning** tasks.

### Mapping Strategy
To ensure schema consistency, we mapped TED_2020 columns to match TED_2017:

```json
{
  "url__webpage": "url",
  "talk__name": "title", 
  "talk__description": "description",
  "speaker__name": "speaker",
  "speaker__description": "speaker_occupation",
  "view_count": "views",
  "recording_date": "recorded_date",
  "talks__tags": "tags"
}
