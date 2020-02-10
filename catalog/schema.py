import graphene
from graphene_django import DjangoObjectType

from .models import Skill, Lesson, Course, Track


# Types
class SkillType(DjangoObjectType):
    class Meta:
        model = Skill


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class TrackType(DjangoObjectType):
    class Meta:
        model = Track


# Queries
class Query(graphene.ObjectType):
    skills = graphene.List(SkillType)
    lessons = graphene.List(LessonType)
    courses = graphene.List(CourseType)
    tracks = graphene.List(TrackType)

    def resolve_skills(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Skill.objects.all()
        if search:
            filter = (
                    Q(key__icontains=search) |
                    Q(name__icontains=search)
            )
            qs = qs.filter(filter)
        if skip:
            qs = qs[skip::]
        if first:
            qs = qs[:first]
        return qs

    def resolve_lessons(self, info, search=None, first=None, skip=None, **kwargs):
        ql = Lesson.objects.all()
        if search:
            filter = (
                    Q(key__icontains=search) |
                    Q(title__icontains=search) |
                    Q(description__icontains=search)
            )
            ql = ql.filter(filter)
        if skip:
            ql = ql[skip::]
        if first:
            ql = ql[:first]
        return ql

    def resolve_courses(self, info, search=None, first=None, skip=None, **kwargs):
        qc = Course.objects.all()
        if search:
            filter = (
                    Q(key__icontains=search) |
                    Q(title__icontains=search) |
                    Q(subtitle__icontains=search) |
                    Q(short_summary__icontains=search) |
                    Q(summary__icontains=search)
            )
            qc = qc.filter(filter)
        if skip:
            qc = qc[skip::]
        if first:
            qc = qc[:first]
        return qc

    def resolve_tracks(self, info, **kwargs):
        return Track.objects.all()


# Mutations
class CreateSkill(graphene.Mutation):
    key = graphene.String()
    name = graphene.String()

    class Arguments:
        key = graphene.String()
        name = graphene.String()

    def mutate(self, info, key, name):
        skill = Skill(key=key, name=name)
        skill.save()

        return CreateSkill(
            key=skill.key,
            name=skill.name
        )


class CreateLesson(graphene.Mutation):
    key = graphene.String()
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()

    class Arguments:
        key = graphene.String()
        title = graphene.String()
        description = graphene.String()
        image = graphene.String()

    def mutate(self, info, key, title, description, image):
        lesson = Lesson(key=key, title=title, description=description, image=image)
        lesson.save()

        return CreateLesson(
            key=lesson.key,
            title=lesson.title,
            description=lesson.description,
            image=lesson.image
        )


class CreateCourse(graphene.Mutation):
    key = graphene.String()
    title = graphene.String()
    subtitle = graphene.String()
    banner_image = graphene.String()
    featured = graphene.Boolean()
    short_summary = graphene.String()
    required_knowledge = graphene.String()
    syllabus = graphene.String()
    homepage = graphene.String()
    summary = graphene.String()
    faq = graphene.String()
    level = graphene.String()
    expected_duration_unit = graphene.String()
    expected_duration = graphene.Int()
    lessons = graphene.List(LessonType)

    class Arguments:
        key = graphene.String()
        title = graphene.String()
        subtitle = graphene.String()
        banner_image = graphene.String()
        featured = graphene.Boolean()
        short_summary = graphene.String()
        required_knowledge = graphene.String()
        syllabus = graphene.String()
        homepage = graphene.String()
        summary = graphene.String()
        faq = graphene.String()
        level = graphene.String()
        expected_duration_unit = graphene.String()
        expected_duration = graphene.Int()
        lesson_id = graphene.String()

    def mutate(self,
               info, key, title, subtitle, banner_image, featured,
               short_summary, required_knowledge, syllabus, homepage,
               summary, faq, level, expected_duration_unit, expected_duration, lesson_id):
        lesson = Lesson.objects.filter(key=lesson_id).first()
        if not lesson:
            raise Exception('Invalid Lesson selected for this course!')

        course = Course.objects.create(
            key=key,
            title=title,
            subtitle=subtitle,
            banner_image=banner_image,
            featured=featured,
            short_summary=short_summary,
            required_knowledge=required_knowledge,
            syllabus=syllabus,
            homepage=homepage,
            summary=summary,
            faq=faq,
            level=level,
            expected_duration_unit=expected_duration_unit,
            expected_duration=expected_duration,
        )
        course.lessons.add(lesson)
        return CreateCourse(
            key=key,
            title=title,
            subtitle=subtitle,
            banner_image=banner_image,
            featured=featured,
            short_summary=short_summary,
            required_knowledge=required_knowledge,
            syllabus=syllabus,
            homepage=homepage,
            summary=summary,
            faq=faq,
            level=level,
            expected_duration_unit=expected_duration_unit,
            expected_duration=expected_duration,
            lessons=lesson
        )


class CreateTrack(graphene.Mutation):
    key = graphene.String()
    name = graphene.String()
    level = graphene.String()
    description = graphene.String()
    short_description = graphene.String()
    display_title = graphene.String()
    # courses = graphene.String()
    # skills = graphene.String()

    class Arguments:
        key = graphene.String()
        name = graphene.String()
        level = graphene.String()
        description = graphene.String()
        short_description = graphene.String()
        display_title = graphene.String()
        # courses = graphene.Field(Course)
        # skills = graphene.Field(Skill)

    def mutate(self, info, key, name, level, description, short_description,
               display_title):
        # course = Course.objects.filter(key=course_id).first()
        # if not course:
        #     raise Exception('Invalid course ID selected for Track')
        # skill = Skill.objects.filter(key=skill_id).first()
        # if not skill:
        #     raise Exception('Invalid skill ID selected for Track')

        Track.objects.create(
            key=key,
            name=name,
            level=level,
            description=description,
            short_description=short_description,
            display_title=display_title,
            # courses=course,
            # skills=skill
        )

        return CreateTrack(
            key=key,
            name=name,
            level=level,
            description=description,
            short_description=short_description,
            display_title=display_title,
            # courses=course,
            # skills=skill
        )


class Mutation(graphene.ObjectType):
    create_skill = CreateSkill.Field()
    create_lesson = CreateLesson.Field()
    create_course = CreateCourse.Field()
    create_track = CreateTrack.Field()